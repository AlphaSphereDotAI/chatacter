#!/usr/bin/env python
# coding: utf-8

# In[1]:

from transformers import AutoTokenizer, AutoModelForCausalLM

# In[2]:


model_id = "mistralai/Mistral-7B-Instruct-v0.2"


# In[3]:


model = AutoModelForCausalLM.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)
tokenizer.use_default_system_prompt = False


# In[ ]:


inputs = tokenizer.encode("how are you?", return_tensors="pt")
outputs = model.generate(inputs, max_length=32, num_beams=4, early_stopping=True)


# In[ ]:


tokenizer.decode(outputs[0])

