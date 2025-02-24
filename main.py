from equipe import formarEquipe
import gradio as gr

solicitacao = {
    "disciplina": "Matemática",
    "assunto": "Funções",
    "topicos": ["Função quadrática", "Função exponencial", "Função logarítmica"]
}

def executar_equipe(solicitacao):
    equipe = formarEquipe(solicitacao)  # Aqui, solicitacao precisa ser um dicionário válido
    resultado = equipe.kickoff()
    return resultado

def gradio_interface(disciplina, assunto, topicos):
    solicitacao = {
        "disciplina": disciplina,
        "assunto": assunto,
        "topicos": topicos.split(", ")
    }
    return executar_equipe(solicitacao)

if __name__ == "__main__":
    iface = gr.Interface(
        fn=gradio_interface,
        inputs=[
            gr.Textbox(label="Disciplina"),
            gr.Textbox(label="Assunto"),
            gr.Textbox(label="Tópicos (separados por vírgula)")
        ],
        outputs=gr.Textbox(label="Plano de estudo"),
        title="Plano de estudos com vídeo e motivacional",
        description="Criador de plano de estudos com Mensagem motivacional e Lista de vídeos com três agentes (falta adicionar o recurso dos vídeos).",
        examples=[
            ["Matemática", "Funções", "Função quadrática, Função exponencial, Função logarítmica"],
            ["História", "Revolução Francesa", "Causas, Eventos principais, Consequências"],
            ["Biologia", "Genética", "DNA, RNA, Hereditariedade"]
        ],
        flagging_options=[], 
        css="footer{display:none !important}"
    )
    iface.launch()
