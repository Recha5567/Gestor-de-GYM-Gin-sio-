from utilities import validar_nome, validar_telefone, validar_idade

alunos = []


def listar():
    if not alunos:
        return 204, "Nenhum aluno registado."
    return 200, alunos


def adicionar(nome, idade, telefone):
    if not validar_nome(nome):
        return 400, "Nome inválido."
    if not validar_idade(idade):
        return 400, "Idade inválida."
    if not validar_telefone(telefone):
        return 400, "Telefone inválido."

    aluno = {"nome": nome.title(), "idade": int(idade), "telefone": telefone}
    alunos.append(aluno)
    return 201, aluno


def editar(indice, nome=None, idade=None, telefone=None):
    if not str(indice).isdigit() or not (0 <= int(indice) - 1 < len(alunos)):
        return 404, "Aluno não encontrado."

    a = alunos[int(indice) - 1]

    if nome and not validar_nome(nome):
        return 400, "Nome inválido."
    if idade and not validar_idade(idade):
        return 400, "Idade inválida."
    if telefone and not validar_telefone(telefone):
        return 400, "Telefone inválido."

    if nome:
        a["nome"] = nome.title()
    if idade:
        a["idade"] = int(idade)
    if telefone:
        a["telefone"] = telefone

    return 200, a


def deletar(indice):
    if not str(indice).isdigit() or not (0 <= int(indice) - 1 < len(alunos)):
        return 404, "Aluno não encontrado."
    return 200, alunos.pop(int(indice) - 1)
