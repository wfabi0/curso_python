def q01():
    lista = []
    for i in range(1, 51):
        lista.append(i)
    print(lista)


def q02():
    lista = []
    for i in range(100, 0, -1):
        lista.append(i)
    print(lista)


def q03():
    lista = []
    i = 0
    while len(lista) <= 100:
        if i % 2 != 0:
            lista.append(i)
        i += 1
    print(lista)


def q04():
    lista = []
    for i in range(0, 10):
        num = int(input(f"Digite o {i + 1}º número: "))
        lista.append(num / 2)
    print("Números digitados:", lista)


def q05():
    lista = []
    for i in range(0, 10):
        num = int(input(f"Digite o {i + 1}º número: "))
        lista.append(num * num)
    print("Números digitados ao quadrado:", lista)


def q06():
    gabarito = []
    for i in range(0, 6):
        numero = int(input(f"Digite o {i + 1}º numero: "))
        gabarito.append(numero)

    apostas = []
    for i in range(10):
        numero = int(input(f"Digite o {i + 1}º numero da aposta: "))
        apostas.append(numero)

    acertos = 0
    for i in range(6):
        if gabarito[i] in apostas:
            acertos += 1
    print(f"Você acertou {acertos} números!")
    print("Gabarito:", gabarito)
    print("Apostas:", apostas)


def q07():
    gabarito = []
    for i in range(0, 6):
        numero = int(input(f"Digite o {i + 1}º numero: "))
        gabarito.append(numero)

    apostas = []
    for i in range(10):
        numero = int(input(f"Digite o {i + 1}º numero da aposta: "))
        apostas.append(numero)

    acertos = 0
    for i in range(6):
        if gabarito[i] in apostas:
            acertos += 1
    print(f"Você acertou {acertos} números!")
    print("Gabarito:", gabarito)
    print("Apostas:", apostas)

    if acertos == 6:
        print("Parabéns! Você fez uma sena, completando todos os números!")
    elif acertos == 4:
        print("Você fez um quadra!")
    elif acertos == 5:
        print("Você fez uma quina!")
