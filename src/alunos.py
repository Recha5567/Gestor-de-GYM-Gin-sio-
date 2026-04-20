from utilities import validar_nome, validar_telefone

alunos = []


def listar_alunos():
    if not alunos:
        return 204, "Nenhum aluno cadastrado."
    return 200, alunos


def adicionar_aluno(nome, idade, telefone):
    if not validar_nome(nome):    #AA
        return 400, "Nome invalido"
    if not idade.isdigit() or not (5 <= int(idade) <= 120):
        return 400, "Idade invalida"
    if not validar_telefone(telefone):
        return 400, "Telefone invalido"    #aaa
    aluno = {"nome": nome.title(), "idade": int(idade), "telefone": telefone}
    alunos.append(aluno)
    return 201, aluno


def editar_aluno(indice, nome=None, idade=None, telefone=None):
    if not str(indice).isdigit() or not (0 <= int(indice) - 1 < len(alunos)):
        return 404, "Aluno não encontrado.", []
    a = alunos[int(indice) - 1]
    erros = []
    if nome:
        if validar_nome(nome):
            a['nome'] = nome.title()
        else:
            erros.append("Nome inválido. Mantido anterior.")
    if idade:
        if idade.isdigit() and 5 <= int(idade) <= 120:
            a['idade'] = int(idade)
        else:
            erros.append("Idade inválida. Mantido anterior.")
#a
    if telefone:
        if validar_telefone(telefone):
            a['telefone'] = telefone
        else:
            erros.append("Telefone inválido. Mantido anterior.")
    return 200, a, erros
#aaa

def deletar_aluno(indice):
    if not str(indice).isdigit() or not (0 <= int(indice) - 1 < len(alunos)):
        return 404, "Aluno não encontrado."
    aluno = alunos.pop(int(indice) - 1)
    return 200, aluno
