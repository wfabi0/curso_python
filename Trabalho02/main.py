import os
import mysql.connector

try:
    cnx = mysql.connector.connect(
        host="localhost",
        database="cadastro_alunos",
        user="root",
        password="root"
    )


except mysql.connector.Error as Erro:
    print("Erro:", Erro)
    exit()


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    try:
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Buscar aluno por ID")
        print("4 - Atualizar telefone")
        print("5 - Excluir aluno")
        print("0 - Sair")

        return int(input("Digite uma opção: "))

    except ValueError:
        print()


def cadastrar():
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    telefone = input("Digite o telefone: ")

    try:

        add_user = (
            "INSERT INTO aluno (nome, email, telefone) values(%s, %s, %s)")

        data = (nome, email, telefone)

        cursor = cnx.cursor()
        cursor.execute(add_user, data)
        cnx.commit()
        print("Usuário cadastrado com sucesso!")

    except Exception as er:
        print("Erro ao cadastrar o usuário!")
        print(er)
        cnx.rollback()


def listar():
    try:
        select_user = ("SELECT * FROM aluno")

        cursor = cnx.cursor(dictionary=True)

        cursor.execute(select_user)
        lista = cursor.fetchall()

        for aluno in lista:
            print(
                f"ID: {aluno['id_aluno']} | Nome: {aluno['nome']} | E-mail: {aluno['email']} | Telefone: {aluno['telefone']}")

    except Exception as er:
        print("Erro ao listar alunos!")
        print(er)


def buscar():
    id = int(input("Digite o ID: "))

    try:
        select_id = ("SELECT * FROM aluno WHERE id_aluno = (%s)")

        cursor = cnx.cursor(dictionary=True)

        data = (id,)

        cursor.execute(select_id, data)
        lista = cursor.fetchone()

        if lista:
            print(
                f"ID: {lista['id_aluno']} | Nome: {lista['nome']} | E-mail: {lista['email']} | Telefone: {lista['telefone']}")
        else:
            print(f"Aluno com ID {id} não encontrado no banco de dados.")

    except Exception as er:
        print("Erro ao buscar aluno!")
        print(er)


def atualizar():
    id = int(input("Digite o ID: "))
    tel = input("Digite o telefone para atualizar: ")

    try:
        query = ("UPDATE aluno SET telefone = %s WHERE id_aluno = %s")
        select_id = ("SELECT * FROM aluno WHERE id_aluno = (%s)")

        cursor = cnx.cursor(dictionary=True)

        data = (tel, id)
        data2 = (id,)

        cursor.execute(query, data)  # update

        if cursor.rowcount > 0:
            cnx.commit()

            cursor.execute(select_id, data2)
            aluno = cursor.fetchone()
            print("Telefone atualizado com sucesso!")
            print(
                f"ID: {aluno['id_aluno']} | Nome: {aluno['nome']} | E-mail: {aluno['email']} | Telefone: {aluno['telefone']}")

        else:
            print(f"Aluno com ID {id} não encontrado no banco de dados.")

    except Exception as er:
        print("Erro ao atualizar telefone!")
        print(er)
        cnx.rollback()


def excluir():
    id = int(input("Digite o ID: "))

    try:
        query = ("DELETE FROM aluno WHERE id_aluno = %s")

        cursor = cnx.cursor(dictionary=True)

        data = (id,)

        cursor.execute(query, data)

        if cursor.rowcount > 0:
            cnx.commit()
            print("Aluno deletado com sucesso!")

        else:
            print(f"Aluno com ID {id} não encontrado no banco de dados.")

    except Exception as er:
        print("Erro ao deletar usuário!")
        print(er)
        cnx.rollback()


while True:
    opcao = menu()
    match opcao:
        case 0:
            print("Saindo...")
            cnx.close()
            break
        case 1:
            limpar()
            cadastrar()
        case 2:
            limpar()
            listar()
        case 3:
            limpar()
            buscar()
        case 4:
            limpar()
            atualizar()
        case 5:
            limpar()
            excluir()
        case _:
            limpar()
            print("Opção Inválida!")

    if opcao == 0:
        break
