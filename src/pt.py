trainers = []

def listar():
    if not trainers:
        return 204, "Nenhum personal trainer cadastrado."
    return 200, trainers

def adicionar_pt(nome, especialidade, telefone):
    pt = {"nome": nome, "especialidade": especialidade, "telefone": telefone}
    trainers.append(pt)
    return 201, pt

def editar(indice, nome=None, especialidade=None, telefone=None):
    if not (0 <= indice < len(trainers)):
        return 404, "Trainer não encontrado."
    t = trainers[indice]
    erros = []
    if nome:
        if nome.replace(" ", "").isalpha():
            t['nome'] = nome.title()
        else:
            erros.append("Nome inválido. Mantido anterior.")
    if especialidade:
        t['especialidade'] = especialidade.capitalize()
    if telefone:
        numero = telefone.lstrip("+")
        if numero.isdigit() and 9 <= len(numero) <= 15:
            t['telefone'] = telefone
        else:
            erros.append("Telefone inválido. Mantido anterior.")
    return 200, t, erros

def deletar(indice):
    if not (0 <= indice < len(trainers)):
        return 404, "Trainer não encontrado."
    trainer = trainers.pop(indice)
    return 200, trainer
