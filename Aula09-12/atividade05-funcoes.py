# Atividade 01

def soma_pares(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return a + b
    else:
        return 0

soma_pares_lambda = lambda a, b: a + b if a % 2 == 0 and b % 2 == 0 else 0

# Atividade 02

def quadrado_da_lista(lista):
    return [x ** 2 for x in lista]

quadrado_da_lista_lambda = lambda lista: list(map(lambda x: x ** 2, lista))

# Atividade 03

def media_aluno(notaA, notaB, notaC):
    media = (notaA + notaB + notaC) / 3
    if media >= 7:
        return "Aprovado"
    elif media >= 5 and media < 7:
        return "Recuperação"
    else:
        return "Reprovado"

media_aluno_lambda = lambda notaA, notaB, notaC: "Aprovado" if (notaA + notaB + notaC) / 3 >= 7 else "Recuperação" if (notaA + notaB + notaC) / 3 >= 5 else "Reprovado"

# Atividade 04

def filtrar_menor_idade(idades):
    return [idade for idade in idades if idade < 18]

filtrar_menor_idade_lambda = lambda idades: filter(lambda idade: idade < 18, idades)

# Atividade 05

def celsius_para_fahrenheit(celsius):
    return celsius * 1.8 + 32

celsius_para_fahrenheit_lambda = lambda celsius: celsius * 1.8 + 32

# Atividade 06

def maior_entre_tres(a, b, c):
    return max(a, b, c)

maior_entre_tres_lambda = lambda a, b, c: max(a, b, c)
    