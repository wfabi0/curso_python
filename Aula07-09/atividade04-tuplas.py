def q11():
    tupla = (1, 2, 3, 4, 5)
    print(tupla)


def q12():
    tupla = (
        "Capelinha", "Ipatinga", "Rio de Janeiro",
        "Guanhães", "Belo Horizonte"
    )
    print(tupla[0], tupla[4])


def q13():
    tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print("Maior valor:", max(tupla))
    print("Menor valor:", min(tupla))
    print("Quantidade de elementos:", len(tupla))


def q14():
    tupla1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    tupla2 = (11, 12, 13, 14, 15)
    tupla3 = tupla1 + tupla2
    print(tupla3)


def q15():
    tupla = (1, 2, 3, 4)
    tupla_repetida = tupla * 3
    print(tupla_repetida)


def q16():
    tupla = (5, 10, 15, 10, 20, 10)
    n10 = tupla.count(10)
    i15 = tupla.index(15)
    print("O número 10 aparece", n10, "vezes.")
    print("O índice da primeira ocorrência do número 15 é:", i15)


def q17():
    tupla = (10, 20, 30)
    a, b, c = tupla
    print("a =", a)
    print("b =", b)
    print("c =", c)


def q18():
    notas = ((7, 8, 6), (9, 5, 7), (8, 8, 10))
    primeira_nota_segundo_aluno = notas[1][0]
    media_terceiro_aluno = sum(notas[2]) / len(notas[2])
    print("Primeira nota do segundo aluno:", primeira_nota_segundo_aluno)
    print("Média do terceiro aluno:", media_terceiro_aluno)
