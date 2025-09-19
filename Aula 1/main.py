def q1():
    print("Estou aprendendo python!")


def q2():
    nome = input("Qual é o seu nome? ")
    idade = input("Quantos anos você tem? ")
    print(f"Olá, {nome}! Você tem {idade} anos.")


def q3():
    x = float(input("Digite um número: "))
    y = float(input("Digite outro número: "))
    soma = x + y
    print(f"A soma de {x} e {y} é {soma}.")
    sub = x - y
    print(f"A subtração de {x} por {y} é {sub}.")
    div = x / y
    print(f"A divisão de {x} por {y} é {div}.")
    mult = x * y
    print(f"A multiplicação de {x} por {y} é {mult}.")


def q4():
    nome = input("Qual é o seu nome? ")
    idade = int(input("Quantos anos você tem? "))
    print("Olá,", nome, "| Você tem ", idade, "anos.")


def q5():
    x = int(input("Digite um número: "))
    y = int(input("Digite outro número: "))
    soma = x + y
    print("A soma de", x, "e", y, "é", soma)


def q6():
    x = int(input("Digite um número: "))
    dobro = x * 2
    triplo = x * 3
    metade = x / 2
    print("O dobro de", x, "é", dobro)
    print("O triplo de", x, "é", triplo)
    print("A metade de", x, "é", metade)


def q7():
    saldo = float(input("Qual é o saldo da sua conta bancária? R$ "))
    saldo_em_dolares = saldo / 5
    print("Seu saldo em dólares é: $", saldo_em_dolares)


def q8():
    nome = input("Qual é o seu nome? ")
    idade = int(input("Quantos anos você tem? "))
    cidade = input("Em qual cidade você mora? ")
    print(f"Olá, {nome}! Você tem {idade} anos e mora em {cidade}. \nSeja bem-vindo ao mundo da programação!")


def q9():
    nota_a = float(input("Digite a primeira nota: "))
    nota_b = float(input("Digite a segunda nota: "))
    media = (nota_a + nota_b) / 2
    if (media >= 7):
        print("Aprovado")
    elif (media >= 5 and media <= 6.9):
        print("Recuperação")
    else:
        print("Reprovado")


def menu():
    print("Escolha uma questão para executar (1-9) ou 0 para sair:")
    escolha = int(input("Digite o número da questão: "))
    if (escolha == 0):
        print("Saindo...")
        exit()
    elif (escolha == 1):
        q1()
    elif (escolha == 2):
        q2()
    elif (escolha == 3):
        q3()
    elif (escolha == 4):
        q4()
    elif (escolha == 5):
        q5()
    elif (escolha == 6):
        q6()
    elif (escolha == 7):
        q7()
    elif (escolha == 8):
        q8()
    elif (escolha == 9):
        q9()
    else:
        print("Opção inválida. Tente novamente.")
    return 1

menu()