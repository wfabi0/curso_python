def q01():
    matriz = [[0, 1], [2, 3]]
    for i in range(2):
        for j in range(2):
            print(matriz[i][j])


def q02():
    matriz = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    for i in range(3):
        for j in range(3):
            print(matriz[i][j], end=" ")
        print()


def q03():
    matriz = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    for i in range(3):
        soma = 0
        for j in range(3):
            soma += matriz[i][j]
        print(f"Soma da linha {i + 1}: {soma}")


def q04():
    matriz = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    for j in range(3):
        soma = 0
        for i in range(3):
            soma += matriz[i][j]
        print(f"Soma da coluna {i + 1}: {soma}")


def q05():
    matriz = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    diagonal = 0
    for i in range(3):
        diagonal += matriz[i][i]
    print(f"Soma da diagonal principal: {diagonal}")

    diagonal_secundaria = 0
    for i in range(3):
        diagonal_secundaria += matriz[i][2 - i]
    print(f"Soma da diagonal secundária: {diagonal_secundaria}")


def q06():
    matriz = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]

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
    matriz = []
    for i in range(2):
        for j in range(3):
            nome = str(input(f"Digite o nome da pessoa {i + j + 1}: "))
            matriz.append([nome])

    print("Matriz:")
    for i in range(2):
        for j in range(3):
            print(matriz[i][j])


q07()
