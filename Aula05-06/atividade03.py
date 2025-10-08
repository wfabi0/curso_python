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
