import json
import os
from utilities import validar_nome, validar_telefone

ARQUIVO = "trainers.json"
trainers = carregar_dados()


def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def guardar_dados(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)


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
    guardar_dados(trainers)
    return 201, pt


def editar(id, nome=None, morada=None, telefone=None, email=None, nif=None):
    f = next((f for f in funcionarios if f["id"] == id), None)
    if f is None:
        return 404, "Funcionário não encontrado."
    guardar_dados(trainers)

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

    guardar_dados(trainers)
    return 200, t


def deletar(id):
    f = next((f for f in trainers if f["id"] == id), None)
    if f is None:
        return 404, "Trainer não encontrado."
    trainers.remove(f)
    guardar_dados(trainers)
    return 200, f
