import gradio as gr

def reverter_texto(texto):
    texto_revertido = texto[::-1]
    return texto_revertido, len(texto_revertido)

iface = gr.Interface(
    fn=reverter_texto,
    inputs="text",
    outputs=["text", "number"],
    title = "Reversor de texto",
    description = "Insira um texto para revertê-lo e contar os caracteres"
)

iface.launch()