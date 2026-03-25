

from PT import menu as menu_trainers
from Alunos import menu_alunos

def main():
    while True:
        print("=== Sistema de Academia ===")
        print("1. Gerenciar Personal Trainers")
        print("2. Gerenciar Alunos")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_trainers()  # chama o CRUD de Personal Trainers
        elif opcao == "2":
            menu_alunos()    # chama o CRUD de Alunos
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!\n")

if __name__ == "__main__":
    main()