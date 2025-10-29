import gradio as gr
import math

def fatorial(num):
    if num < 0:
        return "Fatorial não definido para números negativos"
    return math.factorial(num)

iface = gr.Interface(
    fn = fatorial,
    inputs = "number",
    outputs = "text",
    title = "Calculadora de fatorial",
    description = "digite um número para calcular o seu fatorial"
)

iface.launch()