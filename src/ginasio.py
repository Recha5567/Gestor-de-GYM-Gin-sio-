# ========================= ginasios.py =========================

import json
import os
from utilities import validar_nome, validar_telefone, validar_email, validar_nif
from utils import logger

ARQUIVO = "ginasios.json"


def carregar_dados():
    logger.info("A carregar dados dos ginásios")

    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)

    return []


def guardar_dados(dados):
    logger.info("A guardar dados dos ginásios")

    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)


def listar():
    logger.info("Listagem de ginásios solicitada")

    ginasios = carregar_dados()

    if not ginasios:
        logger.warning("Nenhum ginásio registado")
        return 204, "Nenhum ginásio registado."

    return 200, ginasios


def adicionar(nome, morada, telefone, email, nif):
    logger.info(f"Tentativa de adicionar ginásio: {nome}")

    ginasios = carregar_dados()

    if not validar_nome(nome):
        logger.warning(f"Nome inválido: {nome}")
        return 400, "Nome inválido."

    if not morada.strip():
        logger.warning("Morada inválida")
        return 400, "Morada inválida."

    if not validar_telefone(telefone):
        logger.warning(f"Telefone inválido: {telefone}")
        return 400, "Telefone inválido."

    if not validar_email(email):
        logger.warning(f"Email inválido: {email}")
        return 400, "Email inválido."

    if not validar_nif(nif):
        logger.warning(f"NIF inválido: {nif}")
        return 400, "NIF inválido."

    ginasio = {
        "nome": nome.title(),
        "morada": morada.strip().capitalize(),
        "telefone": telefone,
        "email": email.strip().lower(),
        "nif": nif
    }

    ginasios.append(ginasio)

    guardar_dados(ginasios)

    logger.info(f"Ginásio adicionado com sucesso: {nome}")

    return 201, ginasio


def editar(id, nome=None, morada=None, telefone=None, email=None, nif=None):
    logger.info(f"Tentativa de editar ginásio: {id}")

    ginasios = carregar_dados()

    f = next((f for f in funcionarios if f["id"] == id), None)

    if f is None:
        logger.warning(f"Ginásio não encontrado: {id}")
        return 404, "Funcionário não encontrado."

    guardar_dados(ginasios)

    g = ginasios[int(indice) - 1]

    if nome and not validar_nome(nome):
        logger.warning(f"Nome inválido na edição: {nome}")
        return 400, "Nome inválido."

    if telefone and not validar_telefone(telefone):
        logger.warning(f"Telefone inválido na edição: {telefone}")
        return 400, "Telefone inválido."

    if email and not validar_email(email):
        logger.warning(f"Email inválido na edição: {email}")
        return 400, "Email inválido."

    if nif and not validar_nif(nif):
        logger.warning(f"NIF inválido na edição: {nif}")
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

    guardar_dados(ginasios)

    logger.info(f"Ginásio editado com sucesso: {id}")

    return 200, g


def deletar(indice):
    logger.info(f"Tentativa de remover ginásio: {indice}")

    ginasios = carregar_dados()

    if not str(indice).isdigit() or not (0 <= int(indice) - 1 < len(ginasios)):
        logger.warning(f"Ginásio não encontrado para remoção: {indice}")
        return 404, "Ginásio não encontrado."

    removido = ginasios.pop(int(indice) - 1)

    guardar_dados(ginasios)

    logger.info(f"Ginásio removido com sucesso: {indice}")

    return 200, removido
