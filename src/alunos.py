from utils import logger
import json
import os
from utilities import validar_nome, validar_telefone, validar_idade

ARQUIVO = "alunos.json"

def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
            logger.info("A carregar dados dos alunos")
    return []


def guardar_dados(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
logger.info("A guardar dados dos alunos")


def listar():
    logger.info("Listagem de alunos solicitada")
    alunos = carregar_dados()
    if not alunos:
        return 204, "Nenhum aluno registado."
    return 200, alunos


def adicionar(nome, idade, telefone):
    alunos = carregar_dados()
logger.warning(f"Tentativa de adicionar aluno com nome inválido: {nome}")
logger.warning(f"Tentativa de adicionar aluno com idade inválida: {idade}")
logger.warning(f"Tentativa de adicionar aluno com telefone inválido: {telefone}")
    if not validar_nome(nome):
        return 400, "Nome inválido."
    if not validar_idade(idade):
        return 400, "Idade inválida."
    if not validar_telefone(telefone):
        return 400, "Telefone inválido."
logger.info(f"Aluno adicionado: {nome}")

    aluno = {"nome": nome.title(), "idade": int(idade), "telefone": telefone}
    alunos.append(aluno)
    guardar_dados(alunos)
    return 201, aluno


def editar(indice, nome=None, idade=None, telefone=None):
    alunos = carregar_dados()
    if not str(indice).isdigit() or not (0 <= int(indice) - 1 < len(alunos)):
logger.warning(f"Tentativa de editar aluno inexistente: {indice}")
        return 404, "Aluno não encontrado."

    a = alunos[int(indice) - 1]

logger.warning(f"Nome inválido na edição do aluno {indice}: {nome}")
logger.warning(f"Idade inválida na edição do aluno {indice}: {idade}")
logger.warning(f"Telefone inválido na edição do aluno {indice}: {telefone}")
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
logger.info(f"Aluno editado: {indice}")
    guardar_dados(alunos)
    return 200, a


def deletar(indice):
    alunos = carregar_dados()
    if not str(indice).isdigit() or not (0 <= int(indice) - 1 < len(alunos)):
        logger.warning(f"Tentativa de remover aluno inexistente: {indice}")
        return 404, "Aluno não encontrado."
    aluno_removido = alunos.pop(int(indice) - 1)
    logger.info(f"Aluno removido: {indice}")
    guardar_dados(alunos)
    return 200, aluno_removido

