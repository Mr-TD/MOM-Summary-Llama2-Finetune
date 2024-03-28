import gradio as gr
import pickle
from Summarizer_Helper import Summary_Gen

# Function for text summarization
def summarize_text(text):
    # Your text summarization logic here
    summarized_text = Summary_Gen(text)
    return summarized_text

# Input and output components for Gradio interface
inputs = gr.Textbox(lines=10, label="Input Text")
outputs = gr.Textbox(lines=10, label="Summarized Text")

with open('examples.pkl', 'rb') as f:
    example_list = pickle.load(f)

# Gradio interface
gr.Interface(
    fn=summarize_text,
    inputs=inputs,
    outputs=outputs,
    title="Text Summarization",
    description="Enter the text you want to summarize.",
    examples = [example_list],
    allow_flagging='never'
).launch()
