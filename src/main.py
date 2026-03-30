from alunos import listar_alunos, adicionar_aluno, editar_aluno, deletar_aluno
from pt import listar, adicionar, editar, deletar
from utilities import validar_nome, validar_idade, validar_telefone, confirmar_acao

def main():
    print("=== SISTEMA DE GESTÃO ===\n")

    while True:
        print("Escolha a entidade para gerenciar:")
        print("1. Alunos")
        print("2. Personal Trainers")
        print("3. Sair")
        opc = input("Opção: ").strip()

        if opc == "1":
            print("\n--- Alunos ---")
            print("a. Listar")
            print("b. Adicionar")
            print("c. Editar")
            print("d. Deletar")
            escolha = input("Escolha a ação: ").strip().lower()

            if escolha == "a":
                listar_alunos()
            elif escolha == "b":
                adicionar_aluno()
            elif escolha == "c":
                editar_aluno()
            elif escolha == "d":
                deletar_aluno()
            else:
                print("400 Bad Request - Opção inválida.\n")

        elif opc == "2":
            print("\n--- Personal Trainers ---")
            print("a. Listar")
            print("b. Adicionar")
            print("c. Editar")
            print("d. Deletar")
            escolha = input("Escolha a ação: ").strip().lower()

            if escolha == "a":
                listar()
            elif escolha == "b":
                adicionar()
            elif escolha == "c":
                editar()
            elif escolha == "d":
                deletar()
            else:
                print("400 Bad Request - Opção inválida.\n")

        elif opc == "3":
            print("Saindo do sistema...")
            break
        else:
            print("400 Bad Request - Opção inválida.\n")

if __name__ == "__main__":
    main()
