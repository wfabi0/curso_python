def q01():
    frutas = {'maçã', 'banana', 'uva', 'maçã'}
    print(frutas)


def q02():
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    uniao = a.union(b)
    print("União:", uniao)
    intersecao = a.intersection(b)
    print("Interseção:", intersecao)
    diferenca = a.difference(b)
    print("Diferença (a - b):", diferenca)


def q03():
    pares = {0, 2, 4, 6, 8, 10}
    pertence = 6 in pares
    print("O número 6 pertence ao conjunto de números pares:", pertence)


def q04():
    alunos = set()
    alunos.add("Ana")
    alunos.add("Bruno")
    alunos.add("Carla")
    print("Conjunto de alunos após adições:", alunos)
    alunos.remove("Bruno")
    print("Conjunto de alunos após remoção:", alunos)


def q05():
    letras = {'a', 'b', 'c', 'd'}
    for letra in letras:
        print(letra)


def q06():
    conjunto1 = {1, 2, 3}
    conjunto2 = {3, 4, 5}
    uniao = conjunto1 | conjunto2
    intersecao = conjunto1 & conjunto2
    diferenca_simetrica = conjunto1 ^ conjunto2
    print("União (|):", uniao)
    print("Interseção (&):", intersecao)
    print("Diferença Simétrica (^):", diferenca_simetrica)
