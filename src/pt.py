from utilities import validar_nome, validar_telefone, confirmar_acao

trainers = []

def listar():
    if not trainers:
        print("204 No Content - Nenhum personal trainer cadastrado.\n")
        return
    print("\n200 OK - Lista de Personal Trainers:")
    for i, t in enumerate(trainers):
        print(f"{i+1}. Nome: {t['nome']}, Especialidade: {t['especialidade']}, Telefone: {t['telefone']}")
    print()

def adicionar():
    print("\n➕ Adicionar Personal Trainer")
    nome = validar_nome("Nome: ")
    especialidade = input("Especialidade: ").strip()
    telefone = validar_telefone("Telefone: ")

    trainers.append({"nome": nome, "especialidade": especialidade, "telefone": telefone})
    print(f"201 Created - Personal Trainer '{nome}' adicionado!\n")

def editar():
    listar()
    if not trainers:
        return

    entrada = input("Número do trainer a editar: ").strip()
    if not entrada.isdigit():
        print("400 Bad Request - Número inválido.\n")
        return

    i = int(entrada) - 1
    if 0 <= i < len(trainers):
        t = trainers[i]
        print(f"\n✏️ A editar: {t['nome']} (deixe em branco para manter)")

        nome = input(f"Nome ({t['nome']}): ").strip()
        if nome:
            if nome.replace(" ", "").isalpha():
                t['nome'] = nome.title()
            else:
                print("400 Bad Request - Nome inválido. Mantido anterior.")

        especialidade = input(f"Especialidade ({t['especialidade']}): ").strip()
        if especialidade:
            t['especialidade'] = especialidade.capitalize()

        telefone = input(f"Telefone ({t['telefone']}): ").strip()
        if telefone:
            numero = telefone.lstrip("+")
            if numero.isdigit() and 9 <= len(numero) <= 15:
                t['telefone'] = telefone
            else:
                print("400 Bad Request - Telefone inválido. Mantido anterior.")

        print(f"200 OK - Trainer '{t['nome']}' atualizado!\n")
    else:
        print("404 Not Found - Trainer não encontrado.\n")

def deletar():
    listar()
    if not trainers:
        return

    entrada = input("Número do trainer a deletar: ").strip()
    if not entrada.isdigit():
        print("400 Bad Request - Número inválido.\n")
        return

    i = int(entrada) - 1
    if 0 <= i < len(trainers):
        nome = trainers[i]['nome']
        if confirmar_acao(f"Tem a certeza que quer deletar '{nome}'? (s/n): "):
            trainers.pop(i)
            print(f"200 OK - Trainer '{nome}' deletado!\n")
        else:
            print("400 Bad Request - Ação cancelada.\n")
    else:
        print("404 Not Found - Trainer não encontrado.\n")
