from utils import logger
import json
import os
from utilities import validar_nome, validar_telefone, validar_salario, validar_cargo

ARQUIVO = "funcionarios.json"


CARGOS_VALIDOS = ["recepcionista", "limpeza", "gerente"]


def carregar_dados():
    logger.info("A carregar dados dos funcionários")
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def guardar_dados(dados):
    logger.info("A guardar dados dos funcionários")
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)


def listar():
    logger.info("Listagem de funcionários solicitada")
    funcionarios = carregar_dados()
    if not funcionarios:
        return 204, "Nenhum funcionário registado."
    return 200, funcionarios


def adicionar(nome, data_nascimento, telefone, morada, cargo, salario, data_inicio, data_fim, horario, id_gym):
    funcionarios = carregar_dados()
logger.warning(f"Nome inválido ao adicionar funcionário: {nome}")
logger.warning(f"Telefone inválido ao adicionar funcionário: {telefone}")
logger.warning("Morada inválida ao adicionar funcionário")
logger.warning(f"Cargo inválido ao adicionar funcionário: {cargo}")
logger.warning(f"Salário inválido ao adicionar funcionário: {salario}")
logger.warning(f"ID ginásio inválido ao adicionar funcionário: {id_gym}")
    if not validar_nome(nome):
        return 400, "Nome inválido."
    if not validar_telefone(telefone):
        return 400, "Telefone inválido."
    if not morada.strip():
        return 400, "Morada inválida."
    if not validar_cargo(cargo, CARGOS_VALIDOS):
        return 400, f"Cargo inválido. Válidos: {', '.join(CARGOS_VALIDOS)}."
    if not validar_salario(salario):
        return 400, "Salário inválido."
    if not str(id_gym).isdigit():
        return 400, "ID de ginásio inválido."

    funcionario = {
        "nome": nome.title(),
        "data_nascimento": data_nascimento.strip(),
        "telefone": telefone,
        "morada": morada.strip().capitalize(),
        "cargo": cargo.lower(),
        "salario": float(salario),
        "data_inicio": data_inicio.strip(),
        "data_fim": data_fim.strip() if data_fim else None,
        "horario": horario.strip(),
        "id_gym": int(id_gym)
    }
    funcionarios.append(funcionario)
    guardar_dados(funcionarios)
    return 201, funcionario


def editar(id, nome=None, telefone=None, morada=None, cargo=None, salario=None, data_fim=None, horario=None):
    funcionarios = carregar_dados()
    f = next((f for f in funcionarios if f["id"] == id), None)
    if f is None:
        logger.warning(f"Tentativa de editar funcionário inexistente: {id}")
        return 404, "Funcionário não encontrado."

    f = funcionarios[int(indice) - 1]
logger.warning(f"Nome inválido na edição do funcionário {id}: {nome}")
logger.warning(f"Telefone inválido na edição do funcionário {id}: {telefone}")
logger.warning(f"Cargo inválido na edição do funcionário {id}: {cargo}")
logger.warning(f"Salário inválido na edição do funcionário {id}: {salario}")

    return 200, removido
    if nome and not validar_nome(nome):
        return 400, "Nome inválido."
    if telefone and not validar_telefone(telefone):
        return 400, "Telefone inválido."
    if cargo and not validar_cargo(cargo, CARGOS_VALIDOS):
        return 400, f"Cargo inválido. Válidos: {', '.join(CARGOS_VALIDOS)}."
    if salario and not validar_salario(salario):
        return 400, "Salário inválido."

    if nome:
        f["nome"] = nome.title()
    if telefone:
        f["telefone"] = telefone
    if morada:
        f["morada"] = morada.strip().capitalize()
    if cargo:
        f["cargo"] = cargo.lower()
    if salario:
        f["salario"] = float(salario)
    if data_fim:
        f["data_fim"] = data_fim.strip()
    if horario:
        f["horario"] = horario.strip()

    guardar_dados(funcionarios)
    return 200, f


def deletar(indice):
    funcionarios = carregar_dados()
    if not str(indice).isdigit() or not (0 <= int(indice) - 1 < len(funcionarios)):
        logger.warning(f"Tentativa de remover funcionário inexistente: {indice}")
        return 404, "Funcionário não encontrado."
    removido = funcionarios.pop(int(indice) - 1)
    logger.info(f"Funcionário removido: {indice}")
    guardar_dados(funcionarios)

