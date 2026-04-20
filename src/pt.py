from utilities import validar_nome, validar_telefone

trainers = []


def listar():
    if not trainers:
        return 204, "Nenhum personal trainer cadastrado."
    return 200, trainers

#a
def adicionar_pt(nome, especialidade, telefone):
    if not validar_nome(nome):
        return 400, "Nome invalido"
    if not especialidade.strip():
        return 400, "Especialidade invalida"
    if not validar_telefone(telefone):
        return 400, "Telefone invalido"   #a
    pt = {"nome": nome.title(), "especialidade": especialidade.capitalize(), "telefone": telefone}
    trainers.append(pt)
    return 201, pt


def editar(indice, nome=None, especialidade=None, telefone=None):
    if not str(indice).isdigit() or not (0 <= int(indice) - 1 < len(trainers)):
        return 404, "Trainer não encontrado.", []
    t = trainers[int(indice) - 1]
    erros = []
    if nome:
        if validar_nome(nome):
            t['nome'] = nome.title()
        else:
            erros.append("Nome inválido. Mantido anterior.")
    if especialidade:
        t['especialidade'] = especialidade.capitalize()
    if telefone:
        if validar_telefone(telefone):
            t['telefone'] = telefone
        else:
            erros.append("Telefone inválido. Mantido anterior.")
    return 200, t, erros


def deletar(indice):
    if not str(indice).isdigit() or not (0 <= int(indice) - 1 < len(trainers)):
        return 404, "Trainer não encontrado."
    trainer = trainers.pop(int(indice) - 1)
    return 200, trainer
