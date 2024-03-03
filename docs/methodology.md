# Methodology

## Large Language Models

To design and develop effective chatbots that can engage users in natural and personalized conversations, the following guidelines should be considered:

1. Collecting and Processing Data: For each character, gather a substantial dataset of text that reflects their unique speech patterns and personalities. This data can include dialogue, monologue, and other relevant text sources. Using web scraping, we will collect and process data about Einstein and Napoleon, converting it into a Q\&A format.
2. Exploring pre-trained models to leverage existing advancements: Choose appropriate pre-trained large language models, as the foundation for each character's model to save time and resources. list of suggested LLMs:
   1. Phi-2: this offers a readily available foundation for building advanced. this offers a readily available foundation for building advanced CAs.
   2. Llama-2: this is a family of pre-trained and fine-tuned large language models (LLMs) released by Meta AI in 2023. These models are made freely available for research and commercial purposes, which has drawn significant interest in the AI community.
3. Utilizing a multi-model approach to enhance conversational agents: In interactive systems that involve conversational agents, each character can be characterized by their distinctive way of communicating. This can include their word choices, sentence structure, tone, and other linguistic features that help establish their personality and identity. Employing a multi-model approach can enhance the system's ability to generate diverse and character-specific responses.
4. Fine-tuning individual models using a multi-model approach: Create chatbots tailored to the specific characteristics and personalities of each historical figure. Fine-tune each pre-trained model on its respective character-specific dataset. This involves adjusting the model's parameters to optimize its performance on the task of generating text in the style of that character.

***

## Computer Vision

To integrate the computer vision system into our live chat system, we need to add the Talking Face Animator system. Generating realistic talking head videos using a single-face image and audio presents several challenges, including unnatural head movements, distorted expressions, and loss of identity. This paper argues that these issues stem from learning from coupled 2D motion fields. While directly using 3D information can improve realism, it can also lead to stiff expressions and incoherent videos. SadTalker, This work proposes a novel approach, SadTalker, that leverages 3D motion coefficients (head pose, expression) and implicitly modulates a 3D-aware face renderer for generating talking heads.
