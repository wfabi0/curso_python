import random


def q01():
    for i in range(0, 51):
        print(i)


def q02():
    for i in range(100, 0, -1):
        print(i)


def q03():
    for i in range(100, 201):
        print(i)


def q04():
    for i in range(200, 99, -1):
        print(i)


def q05():
    for i in range(1, 501):
        if i % 5 == 0:
            print(i)


def q06():
    for i in range(0, 101):
        if i % 2 != 0:
            print(i)


def q07():
    for i in range(1, 11):
        a = int(input("Digite um número: "))
        print(f"A metade de {a} é {a/2}")


def q08():
    for i in range(1, 11):
        a = int(input("Digite um número: "))
        print(f"O quadrado de {a} é {a*a}")


def q09():
    num = int(input("Digite um número: "))
    maior = 0
    for i in range(num):
        valor = int(input(f"Digite o {i+1}º número: "))
        if valor > maior:
            maior = valor
    print(f"O maior número é {maior}")


def q10():
    soma_positivos = 0
    total_negativos = 0
    for i in range(20):
        a = int(input(f"Digite o {i+1}º número: "))
        if a >= 0:
            soma_positivos += a
        else:
            total_negativos += 1
    print(f"A soma dos números positivos é {soma_positivos}")
    print(f"A quantidade de números negativos é {total_negativos}")


def q11():
    a = float(input("Digite um número real: "))
    b = int(input("Digite outro número porem inteiro e positivo: "))

    if b < 0:
        print("O número deve ser positivo")
        return

    if b == 0:
        print(f"{a} elevado a {b} é 1")
        return

    potencia = a
    for i in range(1, b):
        potencia *= a
    print(f"{a} elevado a {b} é {potencia}")


def q12():
    n = int(input("Digite um número: "))
    for i in range(1, n + 1):
        if i % 2 == 1:
            print(i)


def q13():
    n = int(input("Digite um número: "))
    print(f"Divisores de {n}: ")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)


def q14():
    a = int(input("Digite um número A: "))
    b = int(input("Digite um número B: "))

    soma = 0
    for i in range(a, b + 1):
        soma += i

    print(soma)


def q15():
    n = int(input("Digite um número para ver se ele é primo: "))

    if n < 2:
        print(f"{n} não é primo")
        return

    for i in range(2, n + 1):
        if n % i == 0 and i != n:
            print(f"{n} não é primo")
            return

    print(f"{n} é primo")


def q16():
    n_fat = int(input("Digite um número para ver seu fatorial: "))

    if n_fat < 0:
        print("Número inválido para fatorial")
        return

    fatorial = 1

    for i in range(n_fat, 1, -1):
        fatorial *= i

    print(f"O fatorial de {n_fat} é {fatorial}")


def q17():
    pares_e_multiplos_5 = 0
    for i in (1, 11):
        a = int(input("Digite um número: "))
        if a % 2 == 0 and a % 5 == 0:
            print(f"{a} é par e múltiplo de 5")
            pares_e_multiplos_5 += 1
    print(
        f"A quantidade de números pares e múltiplos de 5 é {pares_e_multiplos_5}")


def q18():
    n = 0
    positivos, negativos, zero = 0
    while n < 20:
        a = int(input("Digite um número: "))
        if a > 0:
            positivos += 1
        elif a < 0:
            negativos += 1
        else:
            zero += 1
        n += 1


def q19():
    n = 1
    while n <= 7:
        if n == 1:
            print("Domingo")
        elif n == 2:
            print("Segunda-feira")
        elif n == 3:
            print("Terça-feira")
        elif n == 4:
            print("Quarta-feira")
        elif n == 5:
            print("Quinta-feira")
        elif n == 6:
            print("Sexta-feira")
        else:
            print("Sábado")
        n += 1


def q20():
    soma = 0

    while soma <= 100:
        n = int(input("Digite um número: "))
        soma += n
    print(f"A soma dos números é {soma}")


def q21():
    senha_correta = "1234"
    tentativa = input("Digite a senha: ")

    while tentativa != senha_correta:
        print("Senha incorreta. Tente novamente.")
        tentativa = input("Digite a senha: ")

    print("Senha correta. Acesso permitido.")


def q22():
    soma_notas = 0
    quantidade_notas = 0
    while True:
        nota = float(input("Digite uma nota entre 0 e 10 (-1 para sair): "))
        if nota == -1:
            break
        if 0 < nota > 10:
            print("Nota inválida. Tente novamente.")
            continue
        print(f"Nota válida: {nota}")
        quantidade_notas += 1
        soma_notas += nota

    media = soma_notas / quantidade_notas
    print(f"A média das notas é {media}")


def q23():
    numero = random.randint(1, 10)
    tentativas = 0
    while True:
        palpite = int(input("Adivinhe o número entre 1 e 10: "))
        tentativas += 1
        if palpite == numero:
            print(
                f"Parabéns! Você acertou o número {numero} em {tentativas} tentativas.")
            break


def q24():
    frase = input("Digite uma frase: ")
    print(f"O tamanho da frase é {len(frase)} caracteres.")


def q25():
    valor_compra = float(input("Digite o valor da compra: "))
    print("Insira os valores dos produtos pagos (0 para sair): ")
    total_pago = 0
    while True:
        valor = float(input("Digite um valor (0 para sair): "))
        if valor == 0:
            break
        total_pago += valor
    if total_pago >= valor_compra:
        troco = total_pago - valor_compra
        print(f"Compra finalizada. Troco: R$ {troco:.2f}")
    else:
        faltante = valor_compra - total_pago
        print(
            f"Valor insuficiente. Faltam R$ {faltante:.2f} para completar a compra.")


def q26():
    while True:
        idade = int(input("Digite sua idade (0 para sair): "))
        if idade == 0:
            break
        if idade < 18:
            print("Você é menor de idade.")
        elif idade >= 18 and idade < 60:
            print("Você é adulto.")
        else:
            print("Você é idoso.")
