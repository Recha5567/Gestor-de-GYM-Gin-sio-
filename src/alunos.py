from utilities import validar_nome, validar_idade, validar_telefone, confirmar_acao

alunos = []

def listar_alunos():
    if not alunos:
        print("204 No Content - Nenhum aluno cadastrado.\n")
        return
    print("\n200 OK - Lista de Alunos:")
    for i, a in enumerate(alunos):
        print(f"{i+1}. Nome: {a['nome']}, Idade: {a['idade']}, Telefone: {a['telefone']}")
    print()

def adicionar_aluno():
    print("\n➕ Adicionar Aluno")
    nome = validar_nome("Nome: ")
    idade = validar_idade("Idade: ")
    telefone = validar_telefone("Telefone: ")

    alunos.append({"nome": nome, "idade": idade, "telefone": telefone})
    print(f"201 Created - Aluno '{nome}' adicionado!\n")

def editar_aluno():
    listar_alunos()
    if not alunos:
        return

    entrada = input("Número do aluno a editar: ").strip()
    if not entrada.isdigit():
        print("400 Bad Request - Número inválido.\n")
        return

    i = int(entrada) - 1
    if 0 <= i < len(alunos):
        a = alunos[i]
        print(f"\n✏️ A editar: {a['nome']} (deixe em branco para manter)")

        nome = input(f"Nome ({a['nome']}): ").strip()
        if nome:
            if nome.replace(" ", "").isalpha():
                a['nome'] = nome.title()
            else:
                print("400 Bad Request - Nome inválido. Mantido anterior.")

        idade = input(f"Idade ({a['idade']}): ").strip()
        if idade:
            if idade.isdigit() and 5 <= int(idade) <= 120:
                a['idade'] = int(idade)
            else:
                print("400 Bad Request - Idade inválida. Mantido anterior.")

        telefone = input(f"Telefone ({a['telefone']}): ").strip()
        if telefone:
            numero = telefone.lstrip("+")
            if numero.isdigit() and 9 <= len(numero) <= 15:
                a['telefone'] = telefone
            else:
                print("400 Bad Request - Telefone inválido. Mantido anterior.")

        print(f"200 OK - Aluno '{a['nome']}' atualizado!\n")
    else:
        print("404 Not Found - Aluno não encontrado.\n")

def deletar_aluno():
    listar_alunos()
    if not alunos:
        return

    entrada = input("Número do aluno a deletar: ").strip()
    if not entrada.isdigit():
        print("400 Bad Request - Número inválido.\n")
        return

    i = int(entrada) - 1
    if 0 <= i < len(alunos):
        nome = alunos[i]['nome']
        if confirmar_acao(f"Tem a certeza que quer deletar '{nome}'? (s/n): "):
            alunos.pop(i)
            print(f"200 OK - Aluno '{nome}' deletado!\n")
        else:
            print("400 Bad Request - Ação cancelada.\n")
    else:
        print("404 Not Found - Aluno não encontrado.\n")
