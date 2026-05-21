import json
import os
from utilities import validar_nome, validar_telefone, validar_salario, validar_cargo, logger

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
        logger.warning("Nenhum funcionário registado")
        return 204, "Nenhum funcionário registado."

    return 200, funcionarios


def adicionar(nome, data_nascimento, telefone, morada, cargo, salario, data_inicio, data_fim, horario, id_gym):
    logger.info(f"Tentativa de adicionar funcionário: {nome}")

    funcionarios = carregar_dados()

    if not validar_nome(nome):
        logger.ERROR(f"Nome inválido: {nome}")
        return 400, "Nome inválido."

    if not validar_telefone(telefone):
        logger.ERROR(f"Telefone inválido: {telefone}")
        return 400, "Telefone inválido."

    if not morada.strip():
        logger.ERROR("Morada inválida")
        return 400, "Morada inválida."

    if not validar_cargo(cargo, CARGOS_VALIDOS):
        logger.ERROR(f"Cargo inválido: {cargo}")
        return 400, f"Cargo inválido. Válidos: {', '.join(CARGOS_VALIDOS)}."

    if not validar_salario(salario):
        logger.ERROR(f"Salário inválido: {salario}")
        return 400, "Salário inválido."

    if not str(id_gym).isdigit():
        logger.ERROR(f"ID de ginásio inválido: {id_gym}")
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

    logger.info(f"Funcionário adicionado com sucesso: {nome}")

    return 201, funcionario


def editar(id, nome=None, telefone=None, morada=None, cargo=None, salario=None, data_fim=None, horario=None):
    logger.info(f"Tentativa de editar funcionário: {id}")

    funcionarios = carregar_dados()

    f = next((f for f in funcionarios if f["id"] == id), None)

    if f is None:
        logger.ERROR(f"Funcionário não encontrado: {id}")
        return 404, "Funcionário não encontrado."

    f = funcionarios[int(indice) - 1]

    if nome and not validar_nome(nome):
        logger.ERROR(f"Nome inválido na edição: {nome}")
        return 400, "Nome inválido."

    if telefone and not validar_telefone(telefone):
        logger.ERROR(f"Telefone inválido na edição: {telefone}")
        return 400, "Telefone inválido."

    if cargo and not validar_cargo(cargo, CARGOS_VALIDOS):
        logger.warning(f"Cargo inválido na edição: {cargo}")
        return 400, f"Cargo inválido. Válidos: {', '.join(CARGOS_VALIDOS)}."

    if salario and not validar_salario(salario):
        logger.ERROR(f"Salário inválido na edição: {salario}")
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

    logger.info(f"Funcionário editado com sucesso: {id}")

    return 200, f

def deletar(indice):
    logger.info(f"Tentativa de remover funcionário: {indice}")

    funcionarios = carregar_dados()

    if not str(indice).isdigit() or not (0 <= int(indice) - 1 < len(funcionarios)):
        logger.ERROR(f"Funcionário não encontrado para remoção: {indice}")
        return 404, "Funcionário não encontrado."

    removido = funcionarios.pop(int(indice) - 1)

    guardar_dados(funcionarios)

    logger.info(f"Funcionário removido com sucesso: {indice}")
    return 200, removido
