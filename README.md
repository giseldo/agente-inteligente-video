# Agentes Inteligentes – Plataforma CREWAI

Este repositório tem como objetivo o desenvolvimento de uma aplicação baseada em agentes inteligentes utilizando a plataforma CREWAI. O projeto consiste na criação de três agentes que auxiliarão alunos no processo de aprendizado, fornecendo planos de estudo personalizados, conteúdos relevantes e mensagens motivacionais.

## 📌 Objetivos do Projeto

O projeto visa explorar a construção de agentes inteligentes que interagem de forma autônoma para melhorar a experiência de estudo dos alunos. Cada agente desempenha um papel específico para tornar o aprendizado mais eficiente e motivador.

### 🧠 Agentes Inteligentes Desenvolvidos

1. **Coordenador de Estudos**  
   📚 Responsável por criar um plano de estudos personalizado para o aluno, considerando suas dificuldades em determinadas disciplinas.

2. **Especialista em Conteúdo**  
   🔍 Pesquisará vídeos no YouTube sobre o assunto estudado e retornará os mais relevantes, garantindo materiais de qualidade para o aprendizado.

3. **Motivador**  
   💡 Enviará mensagens motivacionais para incentivar o aluno a manter o foco e a disciplina nos estudos.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11.0**  
- **CREWAI** (Plataforma para criação de agentes inteligentes)  
- **YouTube API** (Para busca de vídeos educativos)  
- **Ambiente virtual (venv)**  
- **Gerenciamento de pacotes com PIP**  

---

## 📌 Instalação e Configuração

Antes de iniciar o desenvolvimento, é necessário configurar o ambiente corretamente.

### Passo 1: Verificando a versão do Python

O projeto requer **Python 3.11.0**. Para verificar a versão instalada:

```sh
python --version
```

Se necessário, faça o download da versão correta em: [Python Downloads](https://www.python.org/downloads/).

### Passo 2: Atualizando o PIP

Para garantir que as dependências sejam instaladas corretamente, atualize o **PIP**:

```sh
python.exe -m pip install --upgrade pip
```

### Passo 3: Criando e Ativando o Ambiente Virtual

Para manter as dependências organizadas e evitar conflitos, utilize um **ambiente virtual**:

#### Criando o ambiente virtual:
```sh
python -m venv venv
```

#### Ativando o ambiente virtual:
- **Windows**:
  ```sh
  venv\Scripts\activate
  ```
- **Linux/macOS**:
  ```sh
  source venv/bin/activate
  ```

Após a ativação, todas as bibliotecas instaladas estarão isoladas dentro desse ambiente.

### Passo 4: Instalando Dependências

Para instalar as bibliotecas necessárias:

```sh
pip install -r requirements.txt
```

Se precisar adicionar pacotes manualmente:

```sh
pip install nome-do-pacote
```

---

## 📖 Como Funciona o Projeto

1. O aluno informa a disciplina e suas dificuldades.  
2. O **Coordenador de Estudos** cria um plano de estudos personalizado.  
3. O **Especialista em Conteúdo** pesquisa vídeos no YouTube sobre o assunto.  
4. O **Motivador** envia mensagens motivacionais ao aluno.  

Essa abordagem permite que o estudante tenha um direcionamento claro, materiais de apoio e incentivo durante seu processo de aprendizado.

---

## 📌 Como Contribuir

Caso deseje contribuir para este projeto, siga estas etapas:

1. **Fork** o repositório.
2. Crie uma **branch** para a sua funcionalidade (`git checkout -b minha-feature`).
3. Faça o **commit** das suas alterações (`git commit -m 'Adiciona nova feature'`).
4. Faça o **push** para a branch (`git push origin minha-feature`).
5. Abra um **Pull Request**.

---

Esse README detalha de forma clara o propósito do projeto, os agentes envolvidos e as instruções de instalação. Caso precise adicionar algo mais específico, me avise! 😊
