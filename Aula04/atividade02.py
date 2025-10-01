import math


def q1():
    numero = int(input("Digite um número inteiro: "))
    if numero > 20:
        print("Número maior que 20")


def q2():
    n1 = int(input("Digite o primeiro número inteiro: "))
    n2 = int(input("Digite o segundo número inteiro: "))
    soma = n1 + n2
    if soma > 10:
        print(f"A soma dos números é {soma}, que é maior que 10.")


def q3():
    n = int(input("Digite um número inteiro: "))
    if n % 2 == 0:
        print(f"O número {n} é par.")
    else:
        print(f"O número {n} é ímpar.")


def q4():
    n = float(input("Digite um número: "))
    if n < 0:
        print("Número negativo.")
    elif n == 0:
        print("Número é zero.")
    else:
        print("Número positivo.")


def q5():
    n = int(input("Digite um número inteiro: "))
    if n >= 0:
        raiz = math.sqrt(n)
        print(f"A raiz quadrada de {n} é {raiz:.2f}.")
    else:
        quadrado = n ** 2
        print(f"O quadrado de {n} é {quadrado}.")


def q6():
    n = int(input("Digite um número inteiro: "))
    if n % 3 == 0:
        print(f"O número {n} é múltiplo de 3.")
    else:
        print(f"O número {n} não é múltiplo de 3.")


def q7():
    n = int(input("Digite um número inteiro: "))
    if n % 5 == 0:
        print(f"O número {n} é múltiplo de 5.")
    else:
        print(f"O número {n} não é múltiplo de 5.")


def q8():
    a = int(input("Digite o primeiro número inteiro: "))
    b = int(input("Digite o segundo número inteiro: "))
    if b == 0:
        print("Erro: Não é possível dividir por zero.")
    elif a % b == 0:
        print(f"O número {a} é divisível de {b}.")
    else:
        print(f"O número {a} não é divisível de {b}.")


def q9():
    a = int(input("Digite o primeiro número inteiro: "))
    b = int(input("Digite o segundo número inteiro: "))
    if a > b:
        print(f"O número {a} é maior que {b}.")
    elif a < b:
        print(f"O número {a} é menor que {b}.")
    else:
        print("Os números são iguais.")


def q10():
    salario_bruto = float(input("Digite o salário bruto: "))
    prestacao = float(input("Digite o valor da prestação: "))
    limite = salario_bruto * 0.3
    if prestacao > limite:
        print("Empréstimo não concedido.")
    else:
        print("Empréstimo concedido.")


def q11():
    a = int(input("Digite o primeiro número inteiro: "))
    b = int(input("Digite o segundo número inteiro: "))
    c = int(input("Digite o terceiro número inteiro: "))

    if a < b and a < c:
        if b < c:
            print(a, b, c)
        else:
            print(a, c, b)
    elif b < a and b < c:
        if a < c:
            print(b, a, c)
        else:
            print(b, c, a)


def q12():
    a = int(input("Digite o primeiro número inteiro: "))
    b = int(input("Digite o segundo número inteiro: "))
    c = int(input("Digite o terceiro número inteiro: "))

    if a > b and a > c:
        if b > c:
            print(a, b, c)
        else:
            print(a, c, b)
    elif b > a and b > c:
        if a > c:
            print(b, a, c)
        else:
            print(b, c, a)


def q13():
    peso = float(input("Digite o peso da pessoa (kg): "))
    altura = float(input("Digite a altura da pessoa (m): "))
    imc = peso / (altura ** 2)

    if imc < 20:
        print(f"IMC: {imc:.2f} - Abaixo do peso")
    elif imc >= 20 and imc < 25:
        print(f"IMC: {imc:.2f} - Peso normal")
    elif imc >= 25 and imc < 30:
        print(f"IMC: {imc:.2f} - Sobrepeso")
    elif imc >= 30 and imc < 40:
        print(f"IMC: {imc:.2f} - Obeso")
    elif imc >= 40:
        print(f"IMC: {imc:.2f} - Obesidade Mórbido")


def q14():
    idade = int(input("Digite a idade do nadador: "))

    if idade >= 65:
        print("Maior de idade")
    elif idade >= 18:
        print("Idoso")
    else:
        print("Menor de idade")


def q15():
    idade = int(input("Digite a idade do nadador: "))

    if idade < 16:
        print("Não eleitor")
    elif (idade >= 16 and idade <= 18) or (idade >= 65):
        print("Eleitor facultativo")
    else:
        print("Eleitor obrigatório")


def q16():
    idade = int(input("Digite a idade do nadador: "))

    if idade <= 10:
        print(f"Valor do Plano: R$ {30:.2f}")
    elif idade > 10 and idade <= 29:
        print(f"Valor do Plano: R$ {60:.2f}")
    elif idade > 29 and idade <= 45:
        print(f"Valor do Plano: R$ {120:.2f}")
    elif idade > 45 and idade <= 59:
        print(f"Valor do Plano: R$ {150:.2f}")
    elif idade > 59 and idade <= 65:
        print(f"Valor do Plano: R$ {250:.2f}")
    elif idade > 65:
        print(f"Valor do Plano: R$ {400:.2f}")
    else:
        print("Idade inválida")


def q17():
    inteiro = int(input("Digite um número inteiro: "))

    if inteiro < 1 or inteiro > 12:
        print("Mês inválido")
    else:
        if inteiro == 1:
            print("Janeiro")
        elif inteiro == 2:
            print("Fevereiro")
        elif inteiro == 3:
            print("Março")
        elif inteiro == 4:
            print("Abril")
        elif inteiro == 5:
            print("Maio")
        elif inteiro == 6:
            print("Junho")
        elif inteiro == 7:
            print("Julho")
        elif inteiro == 8:
            print("Agosto")
        elif inteiro == 9:
            print("Setembro")
        elif inteiro == 10:
            print("Outubro")
        elif inteiro == 11:
            print("Novembro")
        elif inteiro == 12:
            print("Dezembro")


def menu():
    print("Escolha uma questão para executar (1-17) ou 0 para sair:")
    for i in range(1, 18):
        print(f"{i} - Questão {i}")
    print("0 - Sair")
    escolha = int(input("Digite sua escolha: "))
    if escolha == 0:
        print("Saindo...")
        exit()
    elif 1 <= escolha <= 17:
        return escolha


def pausa():
    input("Pressione Enter para continuar...")


while True:
    escolha = menu()
    if escolha == 1:
        q1()
        pausa()
    elif escolha == 2:
        q2()
        pausa()
    elif escolha == 3:
        q3()
        pausa()
    elif escolha == 4:
        q4()
        pausa()
    elif escolha == 5:
        q5()
        pausa()
    elif escolha == 6:
        q6()
        pausa()
    elif escolha == 7:
        q7()
        pausa()
    elif escolha == 8:
        q8()
        pausa()
    elif escolha == 9:
        q9()
        pausa()
    elif escolha == 10:
        q10()
        pausa()
    elif escolha == 11:
        q11()
        pausa()
    elif escolha == 12:
        q12()
        pausa()
    elif escolha == 13:
        q13()
        pausa()
    elif escolha == 14:
        q14()
        pausa()
    elif escolha == 15:
        q15()
        pausa()
    elif escolha == 16:
        q16()
        pausa()
    elif escolha == 17:
        q17()
        pausa()
    else:
        print("Escolha inválida. Tente novamente.")
