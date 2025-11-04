alunos = []


def Cadastrar_aluno():
    Nome = input("Escreva seu nome: ")
    idade = int(input("Digite sua idade: "))
    curso = input("Qual o seu curso? ")
    notas = []
    for i in range(3):
        nota = float(input(f"Insira sua nota {i+1}: "))
        notas.append(nota)
    aluno = {
        "nome": Nome,
        "idade": idade,
        "curso": curso,
        "notas": notas
    }
    print("Nome do aluno:", Nome)
    print("Idade do aluno é:", idade)
    print("Curso:", curso)
    for i in range(3):
        print(f"Nota {i+1}: {notas[i]}")

    resposta = input("Você deseja confirmar? (Digite S ou N): ")
    if resposta == "S" or resposta == "s":
        alunos.append(aluno)
        print("Aluno cadastrado com sucesso.")
    else:
        print("Cadastro cancelado.")


def listar_alunos():

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    contador = 1
    for aluno in alunos:
        media = sum(aluno["notas"])/len(aluno["notas"])

        print(
            f"{contador}. {aluno["nome"]} - {aluno["idade"]} anos - {aluno["curso"]} - Média {media} ")
        contador += 1


def exibir_estatistica():
    print("Total de alunos:", len(alunos))
    soma_media_geral = 0
    melhor_media = 0
    pior_media = 10
    for aluno in alunos:
        minha_media = sum(aluno["notas"])/len(aluno["notas"])
        soma_media_geral += minha_media
        if minha_media > melhor_media:
            melhor_media = minha_media
        if minha_media < pior_media:
            pior_media = minha_media

    Media_geral = soma_media_geral / len(alunos)
    print("Media geral de alunos:", Media_geral)
    print("Melhor média:", melhor_media)
    print("Pior média:", pior_media)


def buscar_aluno(nome):
    nome_minusculo = nome.lower()
    for aluno in alunos:
        if nome_minusculo == aluno["nome"]:
            print("Nome do aluno:", aluno["nome"])
            print("Idade do aluno é:", aluno["idade"])
            print("Curso:", aluno["curso"])
            print("Notas:", aluno["notas"])
            return
    print("Aluno não encontrado.")


def excluir_aluno(nome):
    nome_minusculo = nome.lower()
    for aluno in alunos:
        if nome_minusculo == aluno["nome"]:
            print("Nome do aluno:", aluno["nome"])
            print("idade do aluno é:", aluno["idade"])
            print("Curso:", aluno["curso"])
            print("Notas:", aluno["notas"])
            resposta = input("Você deseja remover? (Digite S ou N): ")
            if resposta == "S" or resposta == "s":
                alunos.remove(aluno)
                print("Aluno excluido com sucesso.")
                return
            else:
                print("Exclusão cancelado.")
                return
    print("Aluno não encontrado.")


def menu():
    while (True):
        try:

            print("---------MENU---------")
            print("1. Cadastrar Aluno")
            print("2. Listar alunos")
            print("3. Exibir Estatisticas")
            print("4. Buscar Alunos")
            print("5. Excluir Aluno")
            print("0. Sair")

            opcao = int(input("Escolha sua opção: "))

            if opcao == 1:
                try:
                    Cadastrar_aluno()
                except Exception as error:
                    print(error)
            elif opcao == 2:
                try:
                    listar_alunos()
                except Exception as error:
                    print(error)
            elif opcao == 3:
                try:
                    exibir_estatistica()
                except Exception as error:
                    print(error)
            elif opcao == 4:
                try:
                    nome = input("Insira o nome do aluno: ")
                    buscar_aluno(nome)
                except Exception as error:
                    print(error)
            elif opcao == 5:
                try:
                    nome = input("Insira o nome do aluno: ")
                    excluir_aluno(nome)
                except Exception as error:
                    print(error)
            elif opcao == 0:
                try:
                    print("Saindo do sistema... Até logo!")
                    break
                except Exception as error:
                    print(error)
            else:
                print("Opçao invalida.")
        except Exception as error:
            print(error)


menu()
