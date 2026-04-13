from alunos import listar_alunos, adicionar_aluno, editar_aluno, deletar_aluno
from pt import listar, adicionar_pt, editar, deletar
from utilities import validar_nome, validar_idade, validar_telefone, confirmar_acao

def menu_alunos():
    print("\n--- Alunos ---")
    print("a. Listar")
    print("b. Adicionar")
    print("c. Editar")
    print("d. Deletar")
    escolha = input("Escolha a ação: ").strip().lower()

    if escolha == "a":
        code, resultado = listar_alunos()
        if code == 204:
            print(f"204 No Content - {resultado}\n")
        else:
            print("\n200 OK - Lista de Alunos:")
            for i, a in enumerate(resultado):
                print(f"{i+1}. Nome: {a['nome']}, Idade: {a['idade']}, Telefone: {a['telefone']}")
            print()

    elif escolha == "b":
        print("\n➕ Adicionar Aluno")
        nome = validar_nome("Nome: ")
        idade = validar_idade("Idade: ")
        telefone = validar_telefone("Telefone: ")
        code, aluno = adicionar_aluno(nome, idade, telefone)
        print(f"201 Created - Aluno '{aluno['nome']}' adicionado!\n")

    elif escolha == "c":
        code, resultado = listar_alunos()
        if code == 204:
            print(f"204 No Content - {resultado}\n")
            return
        print("\n200 OK - Lista de Alunos:")
        for i, a in enumerate(resultado):
            print(f"{i+1}. Nome: {a['nome']}, Idade: {a['idade']}, Telefone: {a['telefone']}")
        print()
        entrada = input("Número do aluno a editar: ").strip()
        if not entrada.isdigit():
            print("400 Bad Request - Número inválido.\n")
            return
        i = int(entrada) - 1
        print("(Deixe em branco para manter o valor atual)")
        nome = input("Novo nome: ").strip()
        idade = input("Nova idade: ").strip()
        telefone = input("Novo telefone: ").strip()
        code, resultado, erros = editar_aluno(i, nome, idade, telefone)
        if code == 404:
            print(f"404 Not Found - {resultado}\n")
        else:
            for erro in erros:
                print(f"400 Bad Request - {erro}")
            print(f"200 OK - Aluno '{resultado['nome']}' atualizado!\n")

    elif escolha == "d":
        code, resultado = listar_alunos()
        if code == 204:
            print(f"204 No Content - {resultado}\n")
            return
        print("\n200 OK - Lista de Alunos:")
        for i, a in enumerate(resultado):
            print(f"{i+1}. Nome: {a['nome']}, Idade: {a['idade']}, Telefone: {a['telefone']}")
        print()
        entrada = input("Número do aluno a deletar: ").strip()
        if not entrada.isdigit():
            print("400 Bad Request - Número inválido.\n")
            return
        i = int(entrada) - 1
        nome = resultado[i]['nome'] if 0 <= i < len(resultado) else None
        if nome and confirmar_acao(f"Tem a certeza que quer deletar '{nome}'? (s/n): "):
            code, aluno = deletar_aluno(i)
            if code == 404:
                print(f"404 Not Found - {aluno}\n")
            else:
                print(f"200 OK - Aluno '{aluno['nome']}' deletado!\n")
        else:
            print("400 Bad Request - Ação cancelada.\n")

    else:
        print("400 Bad Request - Opção inválida.\n")


def menu_trainers():
    print("\n--- Personal Trainers ---")
    print("a. Listar")
    print("b. Adicionar")
    print("c. Editar")
    print("d. Deletar")
    escolha = input("Escolha a ação: ").strip().lower()

    if escolha == "a":
        code, resultado = listar()
        if code == 204:
            print(f"204 No Content - {resultado}\n")
        else:
            print("\n200 OK - Lista de Personal Trainers:")
            for i, t in enumerate(resultado):
                print(f"{i+1}. Nome: {t['nome']}, Especialidade: {t['especialidade']}, Telefone: {t['telefone']}")
            print()

    elif escolha == "b":
        print("\n➕ Adicionar Personal Trainer")
        nome = validar_nome("Nome: ")
        especialidade = input("Especialidade: ").strip()
        telefone = validar_telefone("Telefone: ")
        code, pt = adicionar_pt(nome, especialidade, telefone)
        print(f"201 Created - Personal Trainer '{pt['nome']}' adicionado!\n")

    elif escolha == "c":
        code, resultado = listar()
        if code == 204:
            print(f"204 No Content - {resultado}\n")
            return
        print("\n200 OK - Lista de Personal Trainers:")
        for i, t in enumerate(resultado):
            print(f"{i+1}. Nome: {t['nome']}, Especialidade: {t['especialidade']}, Telefone: {t['telefone']}")
        print()
        entrada = input("Número do trainer a editar: ").strip()
        if not entrada.isdigit():
            print("400 Bad Request - Número inválido.\n")
            return
        i = int(entrada) - 1
        print("(Deixe em branco para manter o valor atual)")
        nome = input("Novo nome: ").strip()
        especialidade = input("Nova especialidade: ").strip()
        telefone = input("Novo telefone: ").strip()
        code, resultado, erros = editar(i, nome, especialidade, telefone)
        if code == 404:
            print(f"404 Not Found - {resultado}\n")
        else:
            for erro in erros:
                print(f"400 Bad Request - {erro}")
            print(f"200 OK - Trainer '{resultado['nome']}' atualizado!\n")

    elif escolha == "d":
        code, resultado = listar()
        if code == 204:
            print(f"204 No Content - {resultado}\n")
            return
        print("\n200 OK - Lista de Personal Trainers:")
        for i, t in enumerate(resultado):
            print(f"{i+1}. Nome: {t['nome']}, Especialidade: {t['especialidade']}, Telefone: {t['telefone']}")
        print()
        entrada = input("Número do trainer a deletar: ").strip()
        if not entrada.isdigit():
            print("400 Bad Request - Número inválido.\n")
            return
        i = int(entrada) - 1
        nome = resultado[i]['nome'] if 0 <= i < len(resultado) else None
        if nome and confirmar_acao(f"Tem a certeza que quer deletar '{nome}'? (s/n): "):
            code, trainer = deletar(i)
            if code == 404:
                print(f"404 Not Found - {trainer}\n")
            else:
                print(f"200 OK - Trainer '{trainer['nome']}' deletado!\n")
        else:
            print("400 Bad Request - Ação cancelada.\n")

    else:
        print("400 Bad Request - Opção inválida.\n")


def main():
    print("=== SISTEMA DE GESTÃO ===\n")
    while True:
        print("Escolha a entidade para gerenciar:")
        print("1. Alunos")
        print("2. Personal Trainers")
        print("3. Sair")
        opc = input("Opção: ").strip()

        if opc == "1":
            menu_alunos()
        elif opc == "2":
            menu_trainers()
        elif opc == "3":
            print("Saindo do sistema...")
            break
        else:
            print("400 Bad Request - Opção inválida.\n")

if __name__ == "__main__":
    main()
