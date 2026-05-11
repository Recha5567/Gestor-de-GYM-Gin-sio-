import alunos
import pt
import ginasio
import Funcionário


def mostrar_lista(resultado):
    codigo, dados = resultado
    if codigo != 200:
        print(dados)
        return
    for i, item in enumerate(dados, 1):
        print(f"{i}. {item}")


def mostrar_resultado(resultado):
    codigo, dados = resultado
    if codigo in (200, 201):
        print("Sucesso:", dados)
    else:
        print("Erro:", dados)


# ----- ALUNOS ----
def menu_alunos():
    print("\n1. Listar  2. Adicionar  3. Editar  4. Deletar")
    op = input("Escolha: ").strip()

    if op == "1":
        mostrar_lista(alunos.listar())

    elif op == "2":
        nome = input("Nome: ")
        idade = input("Idade: ")
        telefone = input("Telefone: ")
        mostrar_resultado(alunos.adicionar(nome, idade, telefone))

    elif op == "3":
        mostrar_lista(alunos.listar())
        idx = input("Nº do aluno: ")
        nome = input("Novo nome (enter para manter): ")
        idade = input("Nova idade (enter para manter): ")
        telefone = input("Novo telefone (enter para manter): ")
        mostrar_resultado(alunos.editar(idx, nome or None, idade or None, telefone or None))

    elif op == "4":
        mostrar_lista(alunos.listar())
        idx = input("Nº do aluno: ")
        if input("Confirmar? (s/n): ").lower() == "s":
            mostrar_resultado(alunos.deletar(idx))


# ----- PERSONAL TRAINERS ---

def menu_pt():
    print("\n1. Listar  2. Adicionar  3. Editar  4. Deletar")
    op = input("Escolha: ").strip()

    if op == "1":
        mostrar_lista(pt.listar())

    elif op == "2":
        nome = input("Nome: ")
        especialidade = input("Especialidade: ")
        telefone = input("Telefone: ")
        mostrar_resultado(pt.adicionar(nome, especialidade, telefone))

    elif op == "3":
        mostrar_lista(pt.listar())
        idx = input("Nº do trainer: ")
        nome = input("Novo nome (enter para manter): ")
        especialidade = input("Nova especialidade (enter para manter): ")
        telefone = input("Novo telefone (enter para manter): ")
        mostrar_resultado(pt.editar(idx, nome or None, especialidade or None, telefone or None))

    elif op == "4":
        mostrar_lista(pt.listar())
        idx = input("Nº do trainer: ")
        if input("Confirmar? (s/n): ").lower() == "s":
            mostrar_resultado(pt.deletar(idx))


# ---- GINÁSIOS -----

def menu_ginasios():
    print("\n1. Listar  2. Adicionar  3. Editar  4. Deletar")
    op = input("Escolha: ").strip()

    if op == "1":
        mostrar_lista(ginasios.listar())

    elif op == "2":
        nome = input("Nome: ")
        morada = input("Morada: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        nif = input("NIF: ")
        mostrar_resultado(ginasios.adicionar(nome, morada, telefone, email, nif))

    elif op == "3":
        mostrar_lista(ginasios.listar())
        idx = input("Nº do ginásio: ")
        nome = input("Novo nome (enter para manter): ")
        morada = input("Nova morada (enter para manter): ")
        telefone = input("Novo telefone (enter para manter): ")
        email = input("Novo email (enter para manter): ")
        nif = input("Novo NIF (enter para manter): ")
        mostrar_resultado(ginasios.editar(idx, nome or None, morada or None, telefone or None, email or None, nif or None))

    elif op == "4":
        mostrar_lista(ginasios.listar())
        idx = input("Nº do ginásio: ")
        if input("Confirmar? (s/n): ").lower() == "s":
            mostrar_resultado(ginasios.deletar(idx))


# ---- FUNCIONÁRIOS -----

def menu_funcionarios():
    print("\n1. Listar  2. Adicionar  3. Editar  4. Deletar")
    op = input("Escolha: ").strip()

    if op == "1":
        mostrar_lista(funcionarios.listar())

    elif op == "2":
        nome = input("Nome: ")
        data_nasc = input("Data de nascimento: ")
        telefone = input("Telefone: ")
        morada = input("Morada: ")
        cargo = input("Cargo (recepcionista/limpeza/gerente): ")
        salario = input("Salário: ")
        data_inicio = input("Data de início: ")
        data_fim = input("Data de fim (enter para omitir): ")
        horario = input("Horário: ")
        id_gym = input("ID do ginásio: ")
        mostrar_resultado(funcionarios.adicionar(nome, data_nasc, telefone, morada, cargo, salario, data_inicio, data_fim or None, horario, id_gym))

    elif op == "3":
        mostrar_lista(funcionarios.listar())
        idx = input("Nº do funcionário: ")
        nome = input("Novo nome (enter para manter): ")
        telefone = input("Novo telefone (enter para manter): ")
        morada = input("Nova morada (enter para manter): ")
        cargo = input("Novo cargo (enter para manter): ")
        salario = input("Novo salário (enter para manter): ")
        data_fim = input("Nova data de fim (enter para manter): ")
        horario = input("Novo horário (enter para manter): ")
        mostrar_resultado(funcionarios.editar(idx, nome or None, telefone or None, morada or None, cargo or None, salario or None, data_fim or None, horario or None))

    elif op == "4":
        mostrar_lista(funcionarios.listar())
        idx = input("Nº do funcionário: ")
        if input("Confirmar? (s/n): ").lower() == "s":
            mostrar_resultado(funcionarios.deletar(idx))


# ---- MAIN -----

def main():
    menus = {
        "1": ("Alunos", menu_alunos),
        "2": ("Personal Trainers", menu_pt),
        "3": ("Ginásios", menu_ginasios),
        "4": ("Funcionários", menu_funcionarios),
    }

    while True:
        print("\n=== SISTEMA ===")
        for k, (nome, _) in menus.items():
            print(f"{k}. {nome}")
        print("5. Sair")

        op = input("Opção: ").strip()
        if op == "5":
            break
        elif op in menus:
            print(f"\n--- {menus[op][0]} ---")
            menus[op][1]()
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
