# TaskTracker

## Descrição do Projeto
O TaskTracker é um sistema de gerenciamento de tarefas em linha de comando (CLI) desenvolvido em Python. Seu objetivo é facilitar e centralizar a organização de tarefas, permitindo o cadastro, visualização, conclusão e filtragem de atividades diárias de forma eficiente e estruturada.

## Funcionalidades
- **Cadastrar nova tarefa:** Permite a inserção de título (obrigatório), descrição, prioridade (Alta, Média, Baixa) e data limite.
- **Visualizar todas as tarefas:** Exibe a lista completa de tarefas registradas na memória durante a execução atual.
- **Concluir uma tarefa:** Permite alterar o status de uma tarefa específica de "Pendente" para "Concluída".
- **Filtrar tarefas:** Oferece filtros para exibir tarefas por status (Pendente ou Concluída) ou por nível de prioridade (Alta, Média, Baixa).

## Estrutura do Repositório
```text
Bootcamp-II/
├── docs/
│   └── Entrega Inicial - Bootcamp II-1.pdf
├── src/
│   └── main.py
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Requisitos
- Docker
- Docker Compose

## Passo a Passo de Execução (Guia Docker)

O projeto está totalmente conteinerizado, garantindo que seja executado de forma idêntica e sem falhas em qualquer ambiente de produção, não havendo necessidade de instalar o Python diretamente na máquina hospedeira.

Siga os comandos abaixo no seu terminal, garantindo que você esteja na raiz do diretório do projeto (`Bootcamp-II/`).

**1. Como construir a imagem:**
Este comando lê o arquivo `Dockerfile` e empacota a aplicação e suas dependências. Deve ser executado na primeira vez ou sempre que houver alterações no código-fonte.
```bash
docker build -t tasktracker .
```

**2. Como rodar o container em modo isolado:**
Este comando inicia o container de forma interativa. O uso da flag `-it` é obrigatório para que a entrada de dados (`input()`) da aplicação funcione corretamente no terminal.
```bash
docker run -it tasktracker
```

**3. Como rodar via orquestração (Recomendado):**
Este comando utiliza o arquivo `docker-compose.yml`, que já está configurado para orquestrar a execução interativa da CLI (alocando os canais de entrada e o terminal virtual automaticamente).
```bash
docker compose run tasktracker-app
```

## Instruções de Uso da Aplicação
Após iniciar o container utilizando um dos comandos de execução (`docker run` ou `docker compose run`), o menu interativo da aplicação será exibido no seu terminal. 
1. Digite o número correspondente à opção desejada (de 1 a 5).
2. Pressione `Enter` para confirmar.
3. Siga as instruções na tela para preencher os dados das tarefas (título, descrição, prioridade, data limite).
4. Para encerrar a aplicação e sair do container com segurança, selecione a opção `5` no menu principal.