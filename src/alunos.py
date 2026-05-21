# ========================= alunos.py =========================

import json
import os
from utilities import validar_nome, validar_telefone, validar_idade, logger


ARQUIVO = "alunos.json"

def carregar_dados():
    logger.info("A carregar dados dos alunos")
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def guardar_dados(dados):
    logger.info("A guardar dados dos alunos")
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)




def listar():
    logger.info("Listagem de alunos solicitada")
    alunos = carregar_dados()
    if not alunos:
        logger.error("Nenhum aluno registado")
        return 204, "Nenhum aluno registado."
    return 200, alunos


def adicionar(nome, idade, telefone):
    logger.info(f"Tentativa de adicionar aluno: {nome}")

    alunos = carregar_dados()

    if not validar_nome(nome):
        logger.error(f"Nome inválido: {nome}")
        return 400, "Nome inválido."

    if not validar_idade(idade):
        logger.error(f"Idade inválida: {idade}")
        return 400, "Idade inválida."

    if not validar_telefone(telefone):
        logger.error(f"Telefone inválido: {telefone}")
        return 400, "Telefone inválido."


    aluno = {"nome": nome.title(), "idade": int(idade), "telefone": telefone}
    alunos.append(aluno)

    guardar_dados(alunos)

    logger.info(f"Aluno adicionado com sucesso: {nome}")

    return 201, aluno


def editar(indice, nome=None, idade=None, telefone=None):
    logger.info(f"Tentativa de editar aluno: {indice}")

    alunos = carregar_dados()

    if not str(indice).isdigit() or not (0 <= int(indice) - 1 < len(alunos)):
        logger.error(f"Aluno não encontrado: {indice}")
        return 404, "Aluno não encontrado."

    a = alunos[int(indice) - 1]

    if nome and not validar_nome(nome):
        logger.error(f"Nome inválido na edição: {nome}")
        return 400, "Nome inválido."

    if idade and not validar_idade(idade):
        logger.error(f"Idade inválida na edição: {idade}")
        return 400, "Idade inválida."

    if telefone and not validar_telefone(telefone):
        logger.error(f"Telefone inválido na edição: {telefone}")
        return 400, "Telefone inválido."

    if nome:
        a["nome"] = nome.title()

    if idade:
        a["idade"] = int(idade)

    if telefone:
        a["telefone"] = telefone

    guardar_dados(alunos)

    logger.info(f"Aluno editado com sucesso: {indice}")

    return 200, a


def deletar(indice):
    logger.info(f"Tentativa de remover aluno: {indice}")

    alunos = carregar_dados()

    if not str(indice).isdigit() or not (0 <= int(indice) - 1 < len(alunos)):
        logger.error(f"Aluno não encontrado para remoção: {indice}")
        return 404, "Aluno não encontrado."

    aluno_removido = alunos.pop(int(indice) - 1)

    guardar_dados(alunos)

    logger.info(f"Aluno removido com sucesso: {indice}")

    return 200, aluno_removido
