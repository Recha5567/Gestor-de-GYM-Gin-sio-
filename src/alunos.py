# CRUD simples de Alunos

# Lista que vai armazenar os alunos
alunos = []

# Função para listar todos os alunos
def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.\n")
        return
    print("\nLista de Alunos:")
    for i, a in enumerate(alunos):
        print(f"{i+1}. Nome: {a['nome']}, Idade: {a['idade']}, Telefone: {a['telefone']}")
    print()

# Função para adicionar um aluno
def adicionar_aluno():
    nome = input("Nome: ")
    idade = input("Idade: ")
    telefone = input("Telefone: ")
    alunos.append({"nome": nome, "idade": idade, "telefone": telefone})
    print("Aluno adicionado!")

# Função para editar um aluno
def editar_aluno():
    listar_alunos()
    if not alunos:
        return
    i = int(input("Digite o número do aluno que deseja editar: ")) - 1
    if 0 <= i < len(alunos):
        a = alunos[i]
        a['nome'] = input(f"Nome ({a['nome']}): ") or a['nome']
        a['idade'] = input(f"Idade ({a['idade']}): ") or a['idade']
        a['telefone'] = input(f"Telefone ({a['telefone']}): ") or a['telefone']
        print("Aluno atualizado!")
    else:
        print("Número inválido.")

# Função para deletar um aluno
def deletar_aluno():
    listar_alunos()
    if not alunos:
        return
    i = int(input("Digite o número do aluno que deseja deletar: ")) - 1
    if 0 <= i < len(alunos):
        alunos.pop(i)
        print("Aluno deletado!")
    else:
        print("Número inválido.")

# Menu principal para alunos
def menu_alunos():
    while True:
        print("=== CRUD Alunos ===")
        print("1. Listar")
        print("2. Adicionar")
        print("3. Editar")
        print("4. Deletar")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_alunos()
        elif opcao == "2":
            adicionar_aluno()
        elif opcao == "3":
            editar_aluno()
        elif opcao == "4":
            deletar_aluno()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!\n")

# Executar o menu
if __name__ == "__main__":
    menu_alunos()