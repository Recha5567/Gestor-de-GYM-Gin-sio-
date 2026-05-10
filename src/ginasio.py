from utilities import validar_nome, validar_telefone, validar_email, validar_nif

ginasios = []


def listar():
    if not ginasios:
        return 204, "Nenhum ginásio registado."
    return 200, ginasios


def adicionar(nome, morada, telefone, email, nif):
    if not validar_nome(nome):
        return 400, "Nome inválido."
    if not morada.strip():
        return 400, "Morada inválida."
    if not validar_telefone(telefone):
        return 400, "Telefone inválido."
    if not validar_email(email):
        return 400, "Email inválido."
    if not validar_nif(nif):
        return 400, "NIF inválido."

    ginasio = {
        "nome": nome.title(),
        "morada": morada.strip().capitalize(),
        "telefone": telefone,
        "email": email.strip().lower(),
        "nif": nif
    }
    ginasios.append(ginasio)
    return 201, ginasio


def editar(id, nome=None, morada=None, telefone=None, email=None, nif=None):
    f = next((f for f in funcionarios if f["id"] == id), None)
    if f is None:
        return 404, "Funcionário não encontrado."

    g = ginasios[int(indice) - 1]

    if nome and not validar_nome(nome):
        return 400, "Nome inválido."
    if telefone and not validar_telefone(telefone):
        return 400, "Telefone inválido."
    if email and not validar_email(email):
        return 400, "Email inválido."
    if nif and not validar_nif(nif):
        return 400, "NIF inválido."

    if nome:
        g["nome"] = nome.title()
    if morada:
        g["morada"] = morada.strip().capitalize()
    if telefone:
        g["telefone"] = telefone
    if email:
        g["email"] = email.strip().lower()
    if nif:
        g["nif"] = nif

    return 200, g


def deletar(indice):
    if not str(indice).isdigit() or not (0 <= int(indice) - 1 < len(ginasios)):
        return 404, "Ginásio não encontrado."
    return 200, ginasios.pop(int(indice) - 1)
