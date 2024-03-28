from gpt4all import GPT4All
import textwrap
from IPython.display import Markdown

# Initializing the GPT4All model for the infrence
model = GPT4All("C:/Users/DHARMIK/Desktop/LLM/Ongoing Projects/MOM_Demo/Main/GGUF_Model/Llama-2-7b-MOM_Summar.Q2_K.gguf", allow_download = False, device="cpu")

## Function to convert plain text to markdown format
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Default system prompt for generating conversation summaries
DEFAULT_SYSTEM_PROMPT = """
Below is a conversation between a human and an AI agent. Write a summary of the conversation.
""".strip()

def generate_prompt(
    Transcript: str, system_prompt: str = DEFAULT_SYSTEM_PROMPT
) -> str:
    return f"""### Instruction: {system_prompt}

### Input:
{Transcript.strip()}

### Response:
""".strip()

# To generate summary with the help of fine tune model
def Summary_Gen(Transcript):
    prompt = generate_prompt(Transcript)
    summary = model.generate(prompt=prompt,max_tokens=4096)
    summary_output = to_markdown(summary)
    return summary