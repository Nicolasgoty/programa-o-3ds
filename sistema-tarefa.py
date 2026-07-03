

# Solicita a quantidade de tarefas e converte para inteiro
qtd_tarefas = int(input("Quantas tarefas deseja cadastrar? "))

lista_tarefas = []

# Loop para capturar o nome de cada tarefa
for i in range(qtd_tarefas):
    # Exibe "Digite a tarefa 1:", "Digite a tarefa 2:", etc.
    tarefa = input(f"Digite a tarefa {i + 1}: ")
    lista_tarefas.append(tarefa)


banco_dados_tarefas = []

# Percorre a lista usando enumerate começando do índice 1
for id_tarefa, nome_tarefa in enumerate(lista_tarefas, start=1):
    # Lógica de progressão de prazos (ex: tarefa 1 = 2 dias, tarefa 2 = 4 dias...)
    prazo_dias = id_tarefa * 2
    status = "Pendente"
    
    # Armazena as informações estruturadas em uma tupla
    banco_dados_tarefas.append((id_tarefa, nome_tarefa, prazo_dias, status))


print("\n--- RESUMO DO SISTEMA ---")

# Percorre o banco de dados realizando o desempacotamento de tuplas
for id_tarefa, nome_tarefa, prazo_dias, status in banco_dados_tarefas:
    print(f"ID: {id_tarefa} | Tarefa: {nome_tarefa} | Prazo: {prazo_dias} dias | Status: {status}")

print("-" * 25)
# Exibe a quantidade total de tarefas processadas usando len()
print(f"Total de tarefas gerenciadas: {len(banco_dados_tarefas)}")
