# Related Work

The field of conversational agents (CAs) is rapidly evolving, with a growing emphasis on enhancing their contextual understanding, response generation, and overall engagement. This project explores a multi-pronged approach to achieving these goals.

## Large Language Models

### Conversational Agents with Embodied Avatars

* FurChat: This project explored a similar approach of combining a large language model (LLM) with an embodied avatar for human interaction. FurChat demonstrated the potential for engaging and informative conversations in a physical setting. However, it focused on general information retrieval, not domain-specific assistance.
* ERICA: This project developed an embodied social robot with advanced dialogue capabilities. While not using LLMs, ERICA highlighted the potential of embodied agents for emotional engagement and social interaction.

### Large Language Models in Conversational Agents

* LaMDA: This Google AI project demonstrates the power of LLMs for generating human-like dialogue. However, LaMDA focuses on open-ended conversational scenarios and does not address domain-specific expertise.
* Phi-2: this offers a readily available foundation for building advanced CAs (e.g., \[Radford et al., 2022]). It is a transformer with 2.7 billion parameters. It was trained using the same data sources as Phi-1.5, augmented with a new data source that consists of various NLP synthetic texts and filtered websites (for safety and educational value). When assessed against benchmarks Testing common sense, language understanding, and logical reasoning, Phi-2 highlighted a state-of-the-art performance among models with less than 13 billion parameters. It also employs safety tensors to reduce toxicity and bias in the generated text. It has 24 layers, 32 attention heads, and a hidden size of 40962 with a context length of 2048 tokens. It uses the next-word prediction objective to learn from the training data. In training, it trained on a dataset of size 250B tokens on a 96xA100-80G GPU for 14 days (about 2 weeks), a combination of NLP synthetic data created by AOAI GPT-3.5 and filtered web data from Falcon RefinedWeb and SlimPajama, which was assessed by AOAI GPT-4.
* Llama-2: this is a family of pre-trained and fine-tuned large language models (LLMs) released by Meta AI in 2023. These models are made freely available for research and commercial purposes, which has drawn significant interest in the AI community. It refers to a family of second-generation LLMs developed by Meta. These models are designed for various natural language processing tasks, including dialogue generation and text completion. They are available for both research and commercial use. Llama 2 is an auto-regress language-optimized transformer. The tuned versions use supervised fine-tuning (SFT) and reinforcement learning with human feedback (RLHF) to align with human preferences for helpfulness and safety. It has multiple versions, which are 7B, 13B, and 70B with a context length of 4K tokens.
* Megatron-Turing NLG: This model from NVIDIA highlights the potential of LLMs for factual language generation. However, it primarily focuses on factual summarization and lacks the interactive dialogue capabilities needed for a conversational agent.
* BlenderBot: This Facebook AI project explores LLMs for open-domain dialogue with a focus on factual grounding. While demonstrating progress, it still faces challenges in achieving robust and consistent domain-specific assistance.

### Domain-Specific Conversational Agents&#x20;

Several industries have developed chatbots for specific tasks like customer service or technical support. However, these often lack the embodiment and multi-modal capabilities of your project.

* Mitsuku: This chatbot exhibits impressive performance in open-domain conversation tasks. However, it lacks the embodiment and domain-specific focus of your project
* Cleverbot: This online chatbot learns through user interactions but does not leverage domain-specific knowledge or LLMs.

***

## Computer Vision

### Talking Head Video Generation&#x20;

The creation of talking head videos from a single-face image and speech audio is fraught with challenges, such as unnatural head movements, distorted facial expressions, and modifications to the subject's identity. These issues are attributed to the reliance on learning from coupled 2D motion fields, which can lead to unnatural and incoherent results. Moreover, the use of explicit 3D information has been found to introduce its own set of problems, such as stiff expressions and videos that lack coherence. One of the most powerful models is SadTalker. To address these challenges, SadTalker has been developed. This system generates 3D motion coefficients, including head pose and facial expressions, from audio using a 3D Morphable Model (3DMM) and modulates a novel 3D-aware face render to create talking head videos. SadTalker stands out by explicitly modeling the connections between audio and several types of motion coefficients individually, which helps in achieving more accurate facial expressions and head movements. To learn the realistic motion coefficients, we explicitly model the connections between audio and several types of motion coefficients individually. Precisely, we present ExpNet to learn the accurate facial expression from audio by distilling both coefficients and 3D-rendered faces.

#### Components:

* ExpNet: This component is designed to learn accurate facial expressions directly from audio. It does so by distilling information from both the motion coefficients and 3D-rendered faces, which helps in capturing the nuances of facial expressions that are synchronized with the audio.&#x20;
* PoseVAE: it is a conditional Variational Autoencoder that synthesizes head motion in several styles. This allows for the generation of head movements that are natural and match the speech style, contributing to the video's overall realism.
* 3D Key Points Mapping: The 3D motion coefficients generated by SadTalker are mapped onto an unsupervised 3D key points space of the proposed face render. This mapping is crucial for synthesizing the final video, ensuring that the motion is accurately reflected in the visual output.

#### Benefits:

* Individual Modeling: Explicitly modeling audio-to-motion connections for expression and pose leads to improved realism.
* Distillation-based Learning: ExpNet's learning from both coefficients and rendered faces enhances expression accuracy.
* Style Control: PoseVAE enables generating head motion with several styles based on audio.
* Unsupervised 3D Key Points: Mapping to this space leverages 3D information without introducing stiffness or incoherence.

#### Experiments:&#x20;

Extensive experiments have been conducted to validate the effectiveness of SadTalker. These studies show the method's superiority in motion realism and video quality, outperforming existing approaches in the field. Extensive experiments demonstrate SadTalker's superiority in terms of:&#x20;

* Motion Naturalness: More realistic and varied head motions compared to other methods.
* Expression Quality: Accurate and nuanced facial expressions driven by audio.
* Video Quality: Overall higher perceived quality and identity preservation.
