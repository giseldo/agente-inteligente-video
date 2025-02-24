Agentes Inteligentes
Este repositório tem como objetivo o desenvolvimento de uma aplicação baseada em agentes inteligentes utilizando a plataforma CREWAI. Como parte da atividade proposta pelo professor, foi realizado um estudo sobre a ferramenta, incluindo sua instalação e funcionamento.

📌 Instalação
Antes de iniciar o desenvolvimento, foi necessário garantir que a versão do Python instalada fosse compatível com a plataforma CREWAI. Para isso, foi escolhida a versão 3.11.0, que atende aos requisitos necessários.

Passo 1: Verificando a versão do Python
Para conferir a versão instalada do Python, utilize o seguinte comando:

python --version

Se for necessário instalar ou atualizar o Python, faça o download da versão adequada no site oficial: Python Downloads.

Passo 2: Atualizando o PIP

Após garantir a versão correta do Python, foi realizada a atualização do PIP (gerenciador de pacotes do Python) para a versão mais recente, utilizando o comando:

pip install --upgrade pip

Passo 3: Configuração do Ambiente Virtual

Para manter as dependências organizadas e evitar conflitos com outros projetos, foi criado um ambiente virtual específico para este projeto. Isso pode ser feito com os seguintes comandos:

Criando o ambiente virtual

python -m venv venv

Ativando o ambiente virtual
Windows:
venv\Scripts\activate

Linux/macOS:
source venv/bin/activate

Uma vez ativado o ambiente virtual, todas as bibliotecas instaladas estarão isoladas do sistema global.

Passo 4: Instalando Dependências

Após a configuração inicial, foram instaladas as dependências necessárias para o projeto. Para instalar todas de uma vez, pode-se utilizar um arquivo requirements.txt:

pip install -r requirements.txt

Caso precise adicionar pacotes manualmente, utilize:

pip install nome-do-pacote

🛠️ Tecnologias Utilizadas
Python 3.11.0
CREWAI
Ambiente virtual (venv)
Gerenciamento de pacotes com PIP

📖 Objetivos do Projeto
O projeto busca explorar a construção de agentes inteligentes utilizando a plataforma CREWAI, investigando seus métodos, funcionalidades e integração com aplicações de IA.

📌 Como Contribuir
Caso deseje contribuir para este projeto, siga estas etapas:

Fork o repositório
Crie uma branch para a sua funcionalidade (git checkout -b minha-feature)
Faça o commit das suas alterações (git commit -m 'Adiciona nova feature')
Faça o push para a branch (git push origin minha-feature)
Abra um Pull Request

