from utilities import validar_nome, validar_idade, validar_telefone

alunos = []

def listar_alunos():
    if not alunos:
        return 204, "Nenhum aluno cadastrado."
    return 200, alunos

def adicionar_aluno(nome, idade, telefone):
    aluno = {"nome": nome, "idade": idade, "telefone": telefone}
    alunos.append(aluno)
    return 201, aluno

def editar_aluno(indice, nome=None, idade=None, telefone=None):
    if not (0 <= indice < len(alunos)):
        return 404, "Aluno não encontrado."
    a = alunos[indice]
    erros = []
    if nome:
        if nome.replace(" ", "").isalpha():
            a['nome'] = nome.title()
        else:
            erros.append("Nome inválido. Mantido anterior.")
    if idade:
        if idade.isdigit() and 5 <= int(idade) <= 120:
            a['idade'] = int(idade)
        else:
            erros.append("Idade inválida. Mantido anterior.")
    if telefone:
        numero = telefone.lstrip("+")
        if numero.isdigit() and 9 <= len(numero) <= 15:
            a['telefone'] = telefone
        else:
            erros.append("Telefone inválido. Mantido anterior.")
    return 200, a, erros

def deletar_aluno(indice):
    if not (0 <= indice < len(alunos)):
        return 404, "Aluno não encontrado."
    aluno = alunos.pop(indice)
    return 200, aluno
