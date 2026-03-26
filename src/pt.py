# CRUD simples de Personal Trainer

# Lista que vai armazenar os trainers
trainers = []

# Função para listar todos
def listar():
    if not trainers:
        print("Nenhum personal trainer cadastrado.\n")
        return
    print("\nLista de Personal Trainers:")
    for i, t in enumerate(trainers):
        print(f"{i+1}. Nome: {t['nome']}, Especialidade: {t['especialidade']}, Telefone: {t['telefone']}")
    print()

# Função para adicionar um trainer
def adicionar():
    nome = input("Nome: ")
    especialidade = input("Especialidade: ")
    telefone = input("Telefone: ")
    trainers.append({"nome": nome, "especialidade": especialidade, "telefone": telefone})
    print("Personal trainer adicionado!\n")

# Função para editar um trainer
def editar():
    listar()
    if not trainers:
        return
    i = int(input("Digite o número do trainer que deseja editar: ")) - 1
    if 0 <= i < len(trainers):
        t = trainers[i]
        t['nome'] = input(f"Nome ({t['nome']}): ") or t['nome']
        t['especialidade'] = input(f"Especialidade ({t['especialidade']}): ") or t['especialidade']
        t['telefone'] = input(f"Telefone ({t['telefone']}): ") or t['telefone']
        print("Personal trainer atualizado!\n")
    else:
        print("Número inválido.\n")

# Função para deletar um trainer
def deletar():
    listar()
    if not trainers:
        return
    i = int(input("Digite o número do trainer que deseja deletar: ")) - 1
    if 0 <= i < len(trainers):
        trainers.pop(i)
        print("Personal trainer deletado!\n")
    else:
        print("Número inválido.\n")

# Menu principal
def menu():
    while True:
        print("=== CRUD Personal Trainer ===")
        print("1. Listar")
        print("2. Adicionar")
        print("3. Editar")
        print("4. Deletar")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar()
        elif opcao == "2":
            adicionar()
        elif opcao == "3":
            editar()
        elif opcao == "4":
            deletar()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!\n")

# Executar o menu
if __name__ == "__main__":
    menu()