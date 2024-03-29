import gradio


def response(text):
    return text


with gradio.Blocks() as app:
    with gradio.Column():
        Output = gradio.TextArea(label="Output")
        chat = gradio.Textbox(label="Chat", placeholder="Enter your message here...")
        submit = gradio.Button()
    submit.click(response, chat, Output)


app.launch()
