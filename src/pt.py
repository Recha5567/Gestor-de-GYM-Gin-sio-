from utilities import validar_nome, validar_telefone

trainers = []


def listar():
    if not trainers:
        return 204, "Nenhum personal trainer registado."
    return 200, trainers


def adicionar(nome, especialidade, telefone):
    if not validar_nome(nome):
        return 400, "Nome inválido."
    if not especialidade.strip():
        return 400, "Especialidade inválida."
    if not validar_telefone(telefone):
        return 400, "Telefone inválido."

    pt = {"nome": nome.title(), "especialidade": especialidade.strip().capitalize(), "telefone": telefone}
    trainers.append(pt)
    return 201, pt


def editar(indice, nome=None, especialidade=None, telefone=None):
    if not str(indice).isdigit() or not (0 <= int(indice) - 1 < len(trainers)):
        return 404, "Trainer não encontrado."

    t = trainers[int(indice) - 1]

    if nome and not validar_nome(nome):
        return 400, "Nome inválido."
    if telefone and not validar_telefone(telefone):
        return 400, "Telefone inválido."

    if nome:
        t["nome"] = nome.title()
    if especialidade:
        t["especialidade"] = especialidade.strip().capitalize()
    if telefone:
        t["telefone"] = telefone

    return 200, t


def deletar(indice):
    if not str(indice).isdigit() or not (0 <= int(indice) - 1 < len(trainers)):
        return 404, "Trainer não encontrado."
    return 200, trainers.pop(int(indice) - 1)
