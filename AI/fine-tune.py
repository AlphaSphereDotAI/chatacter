import torch
import transformers
from datasets import load_dataset
from peft import (
    LoraConfig,
    PeftConfig,
    PeftModel,
    get_peft_model,
    prepare_model_for_kbit_training,
)
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
)

torch.set_default_device("cuda")

MODEL_NAME = "microsoft/phi-2"

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto",
    trust_remote_code=True,
    quantization_config=bnb_config,
)

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
tokenizer.pad_token = tokenizer.eos_token

# In[3]:


def print_trainable_parameters(model):
    """Prints the number of trainable parameters in the model."""
    trainable_params = 0
    all_param = 0
    for _, param in model.named_parameters():
        all_param += param.numel()
        if param.requires_grad:
            trainable_params += param.numel()
    print(
        f"trainable params: {trainable_params} || all params: {all_param} || trainables%: {100 * trainable_params / all_param}"
    )


# In[4]:

model.gradient_checkpointing_enable()
model = prepare_model_for_kbit_training(model)

# In[5]:

config = LoraConfig(
    r=16, lora_alpha=32, lora_dropout=0.05, bias="none", task_type="CAUSAL_LM"
)

model = get_peft_model(model, config)
print_trainable_parameters(model)

# # Test original model
#

# In[6]:

prompt = """
<human>: when and where was napoleon born?
<assistant>:
""".strip()

# In[7]:

generation_config = model.generation_config
generation_config.max_new_tokens = 200
generation_config.temperature = 0.7
generation_config.top_p = 0.7
generation_config.num_return_sequences = 1
generation_config.pad_token_id = tokenizer.eos_token_id
generation_config.eos_token_id = tokenizer.eos_token_id

# In[8]:

get_ipython().run_cell_magic(
    "time",
    "",
    'device = "cuda"\n\nencoding = tokenizer(prompt, return_tensors="pt").to(device)\nwith torch.inference_mode():\n    outputs = model.generate(\n        input_ids=encoding.input_ids,\n        attention_mask=encoding.attention_mask,\n        generation_config=generation_config\n    )\n\nprint(tokenizer.decode(outputs[0], skip_special_tokens=True))\n',
)

# # Prep dataset
#

# In[17]:

data = load_dataset(
    "MH0386/napoleon_bonaparte", data_files="napoleon_prompt_format.json"
)

# In[18]:

data

# In[19]:

data["train"][0]

# In[23]:


def generate_prompt(data_point):
    return f"""
<human>: {data_point["Q"]}
<assistant>: {data_point["A"]}
""".strip()


def generate_and_tokenize_prompt(data_point):
    full_prompt = generate_prompt(data_point)
    tokenized_full_prompt = tokenizer(full_prompt, padding=True, truncation=True)
    return tokenized_full_prompt


# In[24]:

data = data["train"].shuffle().map(generate_and_tokenize_prompt)

# In[25]:

data

# # Finetune the model
#

# In[26]:

training_args = transformers.TrainingArguments(
    per_device_train_batch_size=1,
    gradient_accumulation_steps=4,
    num_train_epochs=1,
    learning_rate=2e-4,
    fp16=True,
    save_total_limit=3,
    logging_steps=1,
    output_dir="experiments",
    optim="paged_adamw_8bit",
    lr_scheduler_type="cosine",
    warmup_ratio=0.05,
)

trainer = transformers.Trainer(
    model=model,
    train_dataset=data,
    args=training_args,
    data_collator=transformers.DataCollatorForLanguageModeling(tokenizer, mlm=False),
)
model.config.use_cache = False
trainer.train()

# # Save trained model
#

# In[ ]:

model.save_pretrained("trained-model")

# In[ ]:

PEFT_MODEL = "MH0386/phi-2-napoleon-bonaparte"

model.push_to_hub(PEFT_MODEL, use_auth_token=True)

# In[ ]:

config = PeftConfig.from_pretrained(PEFT_MODEL)
model = AutoModelForCausalLM.from_pretrained(
    config.base_model_name_or_path,
    return_dict=True,
    quantization_config=bnb_config,
    device_map="auto",
    trust_remote_code=True,
)

tokenizer = AutoTokenizer.from_pretrained(config.base_model_name_or_path)
tokenizer.pad_token = tokenizer.eos_token

model = PeftModel.from_pretrained(model, PEFT_MODEL)

# # Run the finetuned model
#

# In[ ]:

generation_config = model.generation_config
generation_config.max_new_tokens = 200
generation_config.temperature = 0.7
generation_config.top_p = 0.7
generation_config.num_return_sequences = 1
generation_config.pad_token_id = tokenizer.eos_token_id
generation_config.eos_token_id = tokenizer.eos_token_id

# In[ ]:

get_ipython().run_cell_magic(
    "time",
    "",
    'device = "cuda:0"\n\nprompt = """\n<human>: midjourney prompt for a boy running in the snow\n<assistant>:\n""".strip()\n\nencoding = tokenizer(prompt, return_tensors="pt").to(device)\nwith torch.inference_mode():\n    outputs = model.generate(\n        input_ids=encoding.input_ids,\n        attention_mask=encoding.attention_mask,\n        generation_config=generation_config\n    )\n\nprint(tokenizer.decode(outputs[0], skip_special_tokens=True))\n',
)
