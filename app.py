from crewai import Agent, Task, Crew, LLM

grocllm = LLM(model="groq/llama-3.3-70b-versatile")

def formarEquipe(assunto):
    
    coordenadorEstudos = Agent(
        role='Coordenador de Estudos',
        goal=f'Criar um plano de estudos personalizado para o 3º ano do ensino médio, focado em {assunto}.',
        backstory='Você é um especialista em educação com experiência em criar planos de estudos eficientes.',
        llm=grocllm
    )
    
    especialistaConteudo = Agent(
        role='Especialista de Conteudo',
        goal=f'Pesquisar vídeos no YouTube relacionados ao assunto de {assunto} para o 3º ano do ensino médio.',
        backstory='Você é um especialista em curadoria de conteúdo educacional.',
        llm=grocllm
    )
    
    motivador = Agent(
        role='Motivador',
        goal='Escrever uma mensagem motivacional para o estudante.',
        backstory='Você é um coach motivacional com experiência em ajudar estudantes a manterem o foco.',
        llm=grocllm
    )
    
    tarefa_coordenadorEstudos = Task(
        description=f'Criar um plano de estudos personalizado para o 3º ano do ensino médio, focado em {assunto}.',
        agent=coordenadorEstudos,
        expected_output='Plano de estudos personalizado.'
    )
    
    tarefa_especialista_conteudo = Task(
        description=f'Pesquisar vídeos no YouTube relacionados ao assunto de {assunto} para o 3º ano do ensino médio.',
        agent=especialistaConteudo,
        expected_output='Lista de vídeos relacionados ao assunto.'
    )
    
    tarefa_motivador = Task(
        description='Escrever uma mensagem motivacional para o estudante.',
        agent=motivador,
        expected_output='Mensagem motivacional.'
    )
    
    equipe = Crew(
        name='Equipe de Estudos',
        members=[coordenadorEstudos, especialistaConteudo, motivador],
        tasks=[tarefa_coordenadorEstudos, tarefa_especialista_conteudo, tarefa_motivador]
    )

    return equipe

def executar_equipe(entrada):
    equipe = formarEquipe(entrada)
    resultado = equipe.kickoff()

    return resultado

if __name__ == "__main__":
    print(executar_equipe('Funções'))  

