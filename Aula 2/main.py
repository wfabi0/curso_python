# idade_str = input("Digite sua idade: ")
# idade_int = int(idade_str)

# print(
#     f"Sua idade é {idade_int} anos. Daqui a um ano você terá {idade_int + 1} anos.")
# print(f"Tipo da variável idade_str: {type(idade_str)}")
# print(f"Tipo da variável idade_int: {type(idade_int)}")


# valor_vazio = ""
# valor_cheio = "Olá"
# numero_zero = 0
# numero_cinco = 5

# print(f"{valor_vazio} é {bool(valor_vazio)}")
# print(f"{valor_cheio} é {bool(valor_cheio)}")
# print(f"{numero_zero} é {bool(numero_zero)}")
# print(f"{numero_cinco} é {bool(numero_cinco)}")

# idade = 30
# print(f"Idade inicial: {idade}")
# idade = 31
# print(f"Idade atualizada: {idade}")

# PI = 3.14159
# TAXA_DE_JUROS = 0.05

# print(f"O valor de PI é {PI}")
# print(f"A taxa de juros é {TAXA_DE_JUROS}")

# Embora o python permita, NÃO devemos alterar o valor de uma constante por convenção
# PI = 3.0 # Isso não é recomendado

##############################################################################################

def atv01():
    contador = 0
    print(f"Contador: {contador}")
    contador += 1
    print(f"Contador: {contador}")
    contador -= 1
    print(f"Contador: {contador}")


def atv02():
    PRECO_UNITARIO = 2.50
    QUANTIDADE = 4
    print(f"Total a pagar: R$ {PRECO_UNITARIO * QUANTIDADE:.2f}")


def atv03():
    A = 10
    B = 20
    A, B = B, A
    print(f"A: {A}, B: {B}")


def atv04():
    numero_str = input("Digite um número: ")
    numero_int = int(numero_str)
    print(f"Resultado da multiplicação por 2: {numero_int * 2}")


def atv05():
    numero_float = 15.75
    numero_float_str = str(numero_float)
    resultante = numero_float_str + " é um número."
    print(resultante)


def atv06():
    nome_completo = input("Digite seu nome completo: ")
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura (em metros): "))
    print(f"{nome} tem {idade} anos e {altura:.2f} metros de altura.")


def menu():
    print("Escolha uma opção de 0 a 6 para executar a respectiva atividade:")
    opcao = int(input())
    if opcao == 0:
        print("Saindo...")
    elif opcao == 1:
        atv01()
    elif opcao == 2:
        atv02()
    elif opcao == 3:
        atv03()
    elif opcao == 4:
        atv04()
    elif opcao == 5:
        atv05()
    elif opcao == 6:
        atv06()
    else:
        print("Opção inválida. Tente novamente.")


menu()
