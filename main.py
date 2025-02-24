from equipe import formarEquipe

solicitacao = {
    "disciplina": "Matemática",
    "assunto": "Funções",
    "topicos": ["Função quadrática", "Função exponencial", "Função logarítmica"]
}

def executar_equipe(solicitacao):
    equipe = formarEquipe(solicitacao)  # Aqui, solicitacao precisa ser um dicionário válido
    resultado = equipe.kickoff()
    return resultado

if __name__ == "__main__":
    print (executar_equipe(solicitacao))  # Passando o dicionário completo, e não apenas a string "Funções"
