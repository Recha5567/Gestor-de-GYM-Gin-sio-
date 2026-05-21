import logging

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    handlers=[
        logging.FileHandler(f"{LOG_DIR}/gestor.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("gestor")


def validar_nome(nome):
    return nome.replace(" ", "").isalpha()


def validar_telefone(telefone):
    numero = telefone.lstrip("+")
    return numero.isdigit() and 9 <= len(numero) <= 15


def validar_email(email):
    return "@" in email and "." in email


def validar_nif(nif):
    return nif.isdigit() and len(nif) == 9


def validar_idade(idade):
    return str(idade).isdigit() and 5 <= int(idade) <= 120


def validar_salario(salario):
    return str(salario).replace(".", "", 1).isdigit() and float(salario) > 0


def validar_cargo(cargo, cargos_validos):
    return cargo.lower() in cargos_validos


def confirmar_acao(msg):
    return input(msg).strip().lower() == "s"
