import gradio as gr
import numpy as np
from PIL import Image
import io
import base64

def criar_slide(titulo, texto, imagem, cor_fundo, cor_texto_paragrafo, cor_titulo):
    
    # Estilo da DIV (container principal)
    estilo_div = (
        f"background-color: {cor_fundo};"
        f"padding: 40px;"
        "min-height: 400px;" 
        "text-align: center;"
    )

    # Estilo específico para o Parágrafo
    estilo_paragrafo = f"color: {cor_texto_paragrafo};"
    
    # Estilo específico para o Título
    estilo_titulo = f"color: {cor_titulo};"

    imagem_html = "" 
    
    # Converte a imagem para base64 se estiver presente
    if imagem is not None:
        try:
            img_pil = Image.fromarray(imagem.astype(np.uint8)) 
            buffered = io.BytesIO()
            img_pil.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            
            imagem_html = (
                f"<img src='data:image/png;base64,{img_str}'"
                "style='max-width: 80%; height: auto; margin-top: 20px;'>"
            )
        except Exception:
            imagem_html = "<p style='color:red;'>Erro ao processar imagem.</p>"
            
    # Aplica os estilos individuais ao H1 e ao P
    slide_html = f"""
    <div style="{estilo_div}">
        <h1 style="{estilo_titulo}">{titulo}</h1> 
        <p style="{estilo_paragrafo}">{texto}</p>
        {imagem_html}
    </div>
    """
    
    return slide_html

iface = gr.Interface(
    fn=criar_slide,
    inputs=[
        gr.Textbox(label="Título do Slide", placeholder="Digite o título...", value="Título Exemplo"),
        gr.Textbox( label="Texto do Slide", placeholder="Digite o texto...", value="Este é um slide de demonstração."),
        gr.Image(type="numpy", label="Imagem do slide"),
        
        # CONFIGURAÇÃO DE CORES INICIAIS
        # 1. Cor de Fundo: Cinza Escuro
        gr.ColorPicker(label="Cor de fundo", value="#444444"), 
        
        # 2. Cor do Parágrafo (Texto do slide): Verde
        gr.ColorPicker(label="Cor do texto do parágrafo", value="#00FF00"), 
        
        # 3. Cor do Título: Cinza Claro
        gr.ColorPicker(label="Cor do título", value="#CCCCCC") 
    ],
    outputs=gr.HTML(label="Slide customizado"),
    title="Criador de Slides com Gradio",
    description="Crie um slide personalizado com cores independentes para fundo, título e parágrafo."
)

iface.launch()