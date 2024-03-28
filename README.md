# MOM-Summary-Llama2-Finetune

## Model description

- **Model type:** Llama-2 7B parameter model fine-tuned on [MOM-Summary](https://huggingface.co/datasets/sasvata/MOM-Summary)  datasets.
- **Language(s):** English
- **License:** Llama 2 Community License
- **Training Precision:** `float16`

## Dataset

- [**MOM-Dataset**](https://huggingface.co/datasets/sasvata/MOM-Summary)

## Quantized ModeL

- [**Llama-2-7b-MOM-Summary-Finetuned-GGUF**](https://huggingface.co/sasvata/Llama2-7b-MOM-Summary-Finetuned-GGUF/blob/main/Llama-2-7b-MOM_Summar.Q2_K.gguf)

## Prompting Format

**Prompt Template Without Input**

```
{system_prompt}

### Instruction:
{instruction or query}

### Response:
{response}
```

## Results

**Input (Transcript):**
```
{
  "date": "2023-03-08",
  "time": "10:00 AM",
  "attendees": ["Manager", "Junior 1", "Junior 2"],
  "transcript": [
    "Manager: Good morning, team. Let's start our daily standup meeting.",
    "Junior 1: Good morning, everyone. Yesterday, I completed the task of setting up the Jenkins pipeline for our new project. Today, I'm going to work on integrating the code with the pipeline.",
    "Junior 2: Good morning. Yesterday, I worked on creating the Docker image for our application. Today, I'll be deploying the application to our staging environment.",
    "Manager: That's great progress. Are there any blockers or challenges that you're facing?",
    "Junior 1: I'm having a bit of trouble configuring the Jenkins pipeline. I'm not sure how to set up the triggers for the pipeline.",
    "Manager: I see. Junior 2, can you help out with that? You've worked with Jenkins before, right?",
    "Junior 2: Sure, I can help. I'll take a look at the pipeline configuration and see if I can figure out the issue.",
    "Manager: Thanks, Junior 2. Junior 1, keep working on integrating the code with the pipeline. If you have any more questions, don't hesitate to ask.",
    "Junior 1: Okay, I will.",
    "Manager: Alright, team. That's it for today's standup meeting. Keep up the good work!",
    "Junior 1 & Junior 2: Thank you, Manager."
  ]
}
```

**Output (Transcript Summary)**
```
Key Points
* The team met for their daily standup on March 8, 2023, at 10:00 AM.

Major Updates
* Junior 1 completed the Jenkins pipeline setup and will integrate code today.
* Junior 2 created the Docker image and will deploy the application to staging.

Priority Tasks
* Junior 1: Troubleshoot Jenkins pipeline configuration.

Current Tasks
* Junior 1: Integrate code with Jenkins pipeline.
* Junior 2: Deploy the application to a staging environment.

Completed Tasks
* Junior 1: Jenkins pipeline setup.
* Junior 2: Docker image creation. 
```

## Usage Note

These models possess impressive linguistic skills, but it's important to remember they haven't been specifically optimized to avoid potentially harmful or offensive content. To mitigate this risk, we advise users to:

- **Exercise discretion**: Carefully consider potential implications before utilizing outputs.
- **Supervise closely**: Monitor outputs, especially in public or sensitive settings.
- **Be aware of limitations**: Remember these models are under development and may not generate perfect results in all situations.

## Meet the researchers

- [**Dharmik Trivedi**](https://huggingface.co/Mr-TD)
- [**Dixit Trivedi**](https://www.linkedin.com/in/dixit-trivedi/)
