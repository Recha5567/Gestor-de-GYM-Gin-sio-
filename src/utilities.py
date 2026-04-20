def validar_nome(nome):
    return nome.replace(" ", "").isalpha()


def validar_telefone(telefone):
    numero = telefone.lstrip("+")
    return numero.isdigit() and 9 <= len(numero) <= 15


def confirmar_acao(msg):
    resp = input(msg).strip().lower()
    return resp == "s"
