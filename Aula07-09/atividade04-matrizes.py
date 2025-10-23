def q01():
    matriz = [[], []]

    for i in range(2):
        for j in range(2):
            numero = int(
                input(f"Digite o valor para a posição [{i}][{j}]: ")
            )
            matriz[i].append(numero)
    print(matriz)


def q02():
    matriz = [[], [], []]
    for i in range(3):
        for j in range(3):
            numero = int(
                input(f"Digite o valor para a posição [{i}][{j}]: ")
            )
            matriz[i].append(numero)

    for i in range(3):
        for j in range(3):
            print(matriz[i][j], end=" ")
        print()


def q03():
    matriz = [[], [], []]
    for i in range(3):
        for j in range(3):
            numero = int(
                input(f"Digite o valor para a posição [{i}][{j}]: ")
            )
            matriz[i].append(numero)

    for i in range(3):
        soma = 0
        for j in range(3):
            soma += matriz[i][j]
        print(f"Soma da linha {i + 1}: {soma}")


def q04():
    matriz = [[], [], []]
    for i in range(3):
        for j in range(3):
            numero = int(
                input(f"Digite o valor para a posição [{i}][{j}]: ")
            )
            matriz[i].append(numero)

    for j in range(3):
        soma = 0
        for i in range(3):
            soma += matriz[i][j]
        print(f"Soma da coluna {i + 1}: {soma}")


def q05():
    matriz = [[], [], []]
    for i in range(3):
        for j in range(3):
            numero = int(
                input(f"Digite o valor para a posição [{i}][{j}]: ")
            )
            matriz[i].append(numero)

    diagonal = 0
    for i in range(3):
        diagonal += matriz[i][i]
    print(f"Soma da diagonal principal: {diagonal}")

    diagonal_secundaria = 0
    for i in range(3):
        diagonal_secundaria += matriz[i][2 - i]
    print(f"Soma da diagonal secundária: {diagonal_secundaria}")


def q06():
    matriz = [[], [], []]
    for i in range(3):
        for j in range(3):
            numero = int(
                input(f"Digite o valor para a posição [{i}][{j}]: ")
            )
            matriz[i].append(numero)

    soma_ref = sum(matriz[0])

    for i in range(3):
        if sum(matriz[i]) != soma_ref:
            print("Não é um quadrado mágico.")
            return

    for j in range(3):
        soma_coluna = sum(matriz[i][j] for i in range(3))
        if soma_coluna != soma_ref:
            print("Não é um quadrado mágico.")
            return

    soma_diag_principal = sum(matriz[i][i] for i in range(3))
    if soma_diag_principal != soma_ref:
        print("Não é um quadrado mágico.")
        return

    soma_diag_secundaria = sum(matriz[i][2 - i] for i in range(3))
    if soma_diag_secundaria != soma_ref:
        print("Não é um quadrado mágico.")
        return

    print("É um quadrado mágico!")


def q07():
    matriz = [[], []]
    pos = 1
    for i in range(2):
        for j in range(3):
            nome = str(input(f"Digite o nome da pessoa {pos}: "))
            matriz[i].append(nome)
            pos += 1

    print("Matriz:", matriz)


def q08():
    matriz = [[], []]
    for i in range(2):
        for j in range(2):
            numero = float(
                input(f"Digite o valor para a posição [{i}][{j}]: ")
            )
            matriz[i].append(numero)

    print(matriz)


def q09():
    matriz1 = [[], []]
    matriz2 = [[], []]
    for i in range(2):
        for j in range(2):
            numero1 = float(
                input(
                    f"Digite o valor para a posição [{i}][{j}] da matriz 1: ")
            )
            matriz1[i].append(numero1)

            numero2 = float(
                input(
                    f"Digite o valor para a posição [{i}][{j}] da matriz 2: ")
            )
            matriz2[i].append(numero2)

    soma_matriz = [[], []]

    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            soma_matriz[i].append(matriz1[i][j] + matriz2[i][j])

    print(soma_matriz)


q09()
