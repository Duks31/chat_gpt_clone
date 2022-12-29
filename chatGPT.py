# importing libraries
import openai
import gradio as gr
from api_secret import API_KEY # importing api key from api_secrets

# Get your API key from openai 
openai.api_key = 'your api key'

start_sequence = "\nAI:"
restart_sequence = "\nHuman:"
prompt = "what is your name"


#main prompt gotten from the openai playground 
def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.5,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text


# the main chatGPT 
def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


#Gradio implementation 
block = gr.Blocks()

with block:
    gr.Markdown("""<h1><center>GPT CLONE</center></h1>""")
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug = True)