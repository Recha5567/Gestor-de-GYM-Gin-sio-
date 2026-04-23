from pt import listar, adicionar_pt
from alunos import listar_alunos, adicionar_aluno, editar_aluno, deletar_aluno


def mostrar_lista(dados, tipo):
    if not dados:
        print("Sem registos.")
        return

    print(f"\nLista de {tipo}:")
    for i, item in enumerate(dados, 1):
        print(f"{i}. {item}")


# ---------------- ALUNOS ----------------

def menu_alunos():
    print("\n--- Alunos ---")
    print("a. Listar")
    print("b. Adicionar")
    print("c. Editar")
    print("d. Deletar")

    escolha = input("Escolha: ").lower()

    if escolha == "a":
        _, alunos = listar_alunos()
        mostrar_lista(alunos, "Alunos")

    elif escolha == "b":
        nome = input("Nome: ")
        idade = input("Idade: ")
        telefone = input("Telefone: ")

        resultado = adicionar_aluno(nome, idade, telefone)
        print(resultado)

    elif escolha == "c":
        _, alunos = listar_alunos()
        mostrar_lista(alunos, "Alunos")

        idx = input("Aluno a editar: ")
        if not idx.isdigit():
            print("Número inválido")
            return

        nome = input("Novo nome: ")
        idade = input("Nova idade: ")
        telefone = input("Novo telefone: ")

        resultado = editar_aluno(idx, nome or None, idade or None, telefone or None)
        print(resultado)

    elif escolha == "d":
        _, alunos = listar_alunos()
        mostrar_lista(alunos, "Alunos")

        idx = input("Aluno a deletar: ")
        if not idx.isdigit():
            print("Número inválido")
            return

        confirmar = input("Confirmar (s/n): ").lower()
        if confirmar == "s":
            resultado = deletar_aluno(idx)
            print(resultado)
        else:
            print("Cancelado")

    else:
        print("Opção inválida")


# ---------------- TRAINERS ----------------

def menu_trainers():
    print("\n--- Personal Trainers ---")
    print("a. Listar")
    print("b. Adicionar")
    print("c. Editar")
    print("d. Deletar")

    escolha = input("Escolha: ").lower()

    if escolha == "a":
        _, pts = listar()
        mostrar_lista(pts, "Personal Trainers")

    elif escolha == "b":
        nome = input("Nome: ")
        especialidade = input("Especialidade: ")
        telefone = input("Telefone: ")

        resultado = adicionar_pt(nome, especialidade, telefone)
        print(resultado)

    elif escolha == "c":
        _, pts = listar()
        mostrar_lista(pts, "Personal Trainers")

        idx = input("Trainer a editar: ")
        if not idx.isdigit():
            print("Número inválido")
            return

        nome = input("Novo nome: ")
        especialidade = input("Nova especialidade: ")
        telefone = input("Novo telefone: ")

        resultado = editar(idx, nome or None, especialidade or None, telefone or None)
        print(resultado)

    elif escolha == "d":
        _, pts = listar()
        mostrar_lista(pts, "Personal Trainers")

        idx = input("Trainer a deletar: ")
        if not idx.isdigit():
            print("Número inválido")
            return

        confirmar = input("Confirmar (s/n): ").lower()
        if confirmar == "s":
            resultado = deletar(idx)
            print(resultado)
        else:
            print("Cancelado")

    else:
        print("Opção inválida")


# ---------------- MAIN ----------------

def main():
    while True:
        print("\n=== SISTEMA ===")
        print("1. Alunos")
        print("2. Trainers")
        print("3. Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            menu_alunos()
        elif opcao == "2":
            menu_trainers()
        elif opcao == "3":
            break
        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()
