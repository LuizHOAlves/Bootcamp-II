import datetime

def exibir_menu():
    print("\n--- Gerenciador de Tarefas ---")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar todas as tarefas")
    print("3. Concluir uma tarefa")
    print("4. Filtrar tarefas")
    print("5. Sair da aplicação")
    return input("Escolha uma opção: ").strip()

def validar_data(data_str):
    if not data_str:
        return False
    try:
        datetime.datetime.strptime(data_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def cadastrar_tarefa(tarefas):
    print("\n--- Cadastro de Nova Tarefa ---")
    
    # Validação do Título
    while True:
        titulo = input("Título (obrigatório): ").strip()
        if titulo:
            break
        print("Erro: O título não pode ser vazio. Tente novamente.")
    
    # Descrição livre
    descricao = input("Descrição (opcional): ").strip()
    
    # Validação de Prioridade (Agora incluindo Baixa)
    prioridades_validas = {"alta": "Alta", "média": "Média", "media": "Média", "baixa": "Baixa"}
    while True:
        p_input = input("Prioridade (Alta, Média, Baixa): ").strip().lower()
        if p_input in prioridades_validas:
            prioridade = prioridades_validas[p_input]
            break
        print("Erro: Prioridade inválida. Digite apenas 'Alta', 'Média' ou 'Baixa'.")
    
    # Validação de Data Limite
    while True:
        data_limite = input("Data limite (DD/MM/AAAA): ").strip()
        if validar_data(data_limite):
            break
        print("Erro: Data inválida ou formato incorreto. Use DD/MM/AAAA para uma data real.")
    
    # Cadastro do dicionário
    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }
    
    tarefas.append(tarefa)
    print("\nSucesso: Tarefa registrada com sucesso!")

def visualizar_tarefas(tarefas, cabecalho="\n--- Tarefas Cadastradas ---"):
    print(cabecalho)
    if not tarefas:
        print("Não existem registros de tarefas no momento para a visualização solicitada.")
        return

    for i, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa #{i}")
        print(f"Título:      {tarefa['titulo']}")
        print(f"Descrição:   {tarefa['descricao'] if tarefa['descricao'] else 'Sem descrição'}")
        print(f"Prioridade:  {tarefa['prioridade']}")
        print(f"Data Limite: {tarefa['data_limite']}")
        print(f"Status:      {tarefa['status']}")
        print("-" * 30)

def concluir_tarefa(tarefas):
    print("\n--- Concluir Tarefa ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    
    visualizar_tarefas(tarefas, cabecalho="Tarefas disponíveis:")
    try:
        indice = int(input("Digite o número da tarefa que deseja marcar como 'Concluída': ").strip())
        if 1 <= indice <= len(tarefas):
            tarefa = tarefas[indice - 1]
            if tarefa["status"] == "Concluída":
                print("Aviso: Esta tarefa já está concluída.")
            else:
                tarefa["status"] = "Concluída"
                print(f"Sucesso: A tarefa '{tarefa['titulo']}' foi marcada como concluída!")
        else:
            print("Erro: Número de tarefa inexistente.")
    except ValueError:
        print("Erro: Por favor, digite um número válido.")

def filtrar_tarefas(tarefas):
    print("\n--- Filtrar Tarefas ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada para filtrar.")
        return

    print("1. Por Status (Pendente / Concluída)")
    print("2. Por Nível de Prioridade (Alta / Média / Baixa)")
    opcao = input("Escolha o tipo de filtro: ").strip()

    tarefas_filtradas = []

    if opcao == '1':
        print("\nQual status deseja visualizar?")
        print("1. Pendente")
        print("2. Concluída")
        status_op = input("Escolha: ").strip()
        
        status_alvo = "Pendente" if status_op == '1' else "Concluída" if status_op == '2' else None
        
        if status_alvo:
            tarefas_filtradas = [t for t in tarefas if t['status'] == status_alvo]
            visualizar_tarefas(tarefas_filtradas, cabecalho=f"\n--- Tarefas Filtradas: {status_alvo} ---")
        else:
            print("Erro: Opção de status inválida.")
            
    elif opcao == '2':
        pri_input = input("\nDigite a prioridade que deseja buscar (Alta, Média, Baixa): ").strip().lower()
        mapa_pri = {"alta": "Alta", "média": "Média", "media": "Média", "baixa": "Baixa"}
        
        if pri_input in mapa_pri:
            prioridade_alvo = mapa_pri[pri_input]
            tarefas_filtradas = [t for t in tarefas if t['prioridade'] == prioridade_alvo]
            visualizar_tarefas(tarefas_filtradas, cabecalho=f"\n--- Tarefas Filtradas: Prioridade {prioridade_alvo} ---")
        else:
            print("Erro: Prioridade inválida.")
    else:
        print("Erro: Opção de filtro inválida.")

def main():
    tarefas = []
    
    while True:
        opcao = exibir_menu()
        
        if opcao == '1':
            cadastrar_tarefa(tarefas)
        elif opcao == '2':
            visualizar_tarefas(tarefas)
        elif opcao == '3':
            concluir_tarefa(tarefas)
        elif opcao == '4':
            filtrar_tarefas(tarefas)
        elif opcao == '5':
            print("Saindo da aplicação. Até logo!")
            break
        else:
            print("Erro: Opção inválida. Escolha uma opção de 1 a 5.")

if __name__ == "__main__":
    main()