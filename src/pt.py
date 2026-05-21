import json
import os
from utilities import validar_nome, validar_telefone
from utils import logger

ARQUIVO = "pt.json"

def carregar_dados():
    logger.info("A carregar dados dos personal trainers")
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def guardar_dados(dados):
    logger.info("A guardar dados dos personal trainers")
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def listar():
    logger.info("Listagem de personal trainers solicitada")
    pts = carregar_dados()

    if not pts:
        logger.warning("Nenhum personal trainer registado")
        return 204, "Nenhum personal trainer registado."

    return 200, pts

def adicionar(nome, especialidade, telefone):
    logger.info(f"Tentativa de adicionar PT: {nome}")
    pts = carregar_dados()

    if not validar_nome(nome):
        logger.warning(f"Nome inválido: {nome}")
        return 400, "Nome inválido."

    if not especialidade.strip():
        logger.warning("Especialidade inválida")
        return 400, "Especialidade inválida."

    if not validar_telefone(telefone):
        logger.warning(f"Telefone inválido: {telefone}")
        return 400, "Telefone inválido."

    pt = {
        "nome": nome.title(),
        "especialidade": especialidade.strip().capitalize(),
        "telefone": telefone
    }

    pts.append(pt)
    guardar_dados(pts)

    logger.info(f"PT adicionado com sucesso: {nome}")

    return 201, pt

def editar(id, nome=None, morada=None, telefone=None, email=None, nif=None):
    logger.info(f"Tentativa de editar PT: {id}")
    pts = carregar_dados()

    f = next((f for f in funcionarios if f["id"] == id), None)

    if f is None:
        logger.warning(f"PT não encontrado: {id}")
        return 404, "Funcionário não encontrado."

    guardar_dados(pts)

    t = pts[int(indice) - 1]

    if nome and not validar_nome(nome):
        logger.warning(f"Nome inválido na edição: {nome}")
        return 400, "Nome inválido."

    if telefone and not validar_telefone(telefone):
        logger.warning(f"Telefone inválido na edição: {telefone}")
        return 400, "Telefone inválido."

    if nome:
        t["nome"] = nome.title()

    if especialidade:
        t["especialidade"] = especialidade.strip().capitalize()

    if telefone:
        t["telefone"] = telefone

    guardar_dados(pts)

    logger.info(f"PT editado com sucesso: {id}")

    return 200, t

def deletar(id):
    logger.info(f"Tentativa de remover PT: {id}")
    pts = carregar_dados()

    f = next((f for f in pts if f["id"] == id), None)

    if f is None:
        logger.warning(f"PT não encontrado para remoção: {id}")
        return 404, "Trainer não encontrado."

    pts.remove(f)
    guardar_dados(pts)

    logger.info(f"PT removido com sucesso: {id}")

    return 200, f
