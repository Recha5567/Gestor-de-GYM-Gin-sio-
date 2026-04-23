from utilities import validar_nome, validar_telefone

alunos = []


def listar_alunos():
    if not alunos:
        return 204, "Nenhum aluno cadastrado."
    return 200, alunos


def adicionar_aluno(nome, idade, telefone):
    if not validar_nome(nome):
        return 400, "Nome invalido"

    if not idade.isdigit() or not (5 <= int(idade) <= 120):
        return 400, "Idade invalida"

    if not validar_telefone(telefone):
        return 400, "Telefone invalido"

    aluno = {
        "nome": nome.title(),
        "idade": int(idade),
        "telefone": telefone
    }
    alunos.append(aluno)
    return 201, aluno


def editar_aluno(indice, nome=None, idade=None, telefone=None):
    if not str(indice).isdigit() or not (0 <= int(indice) - 1 < len(alunos)):
        return 404, "Aluno nao encontrado."

    a = alunos[int(indice) - 1]

    if nome:
        if not validar_nome(nome):
            return 400, "Nome invalido"
        a['nome'] = nome.title()

    if idade:
        if not idade.isdigit() or not (5 <= int(idade) <= 120):
            return 400, "Idade invalida"
        a['idade'] = int(idade)

    if telefone:
        if not validar_telefone(telefone):
            return 400, "Telefone invalido"
        a['telefone'] = telefone

    return 200, a


def deletar_aluno(indice):
    if not str(indice).isdigit() or not (0 <= int(indice) - 1 < len(alunos)):
        return 404, "Aluno nao encontrado."

    aluno = alunos.pop(int(indice) - 1)
    return 200, aluno
