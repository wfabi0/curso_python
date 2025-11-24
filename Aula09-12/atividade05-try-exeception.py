# Atividade 08

import math


def divisao_segura():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")

    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")

    except ValueError:
        print("Erro: Entrada inválida. Por favor, insira números válidos.")


divisao_segura()

# Atividade 09


def abrir_arquivo():
    while True:
        try:
            nome_arquivo = input("Digite o nome do arquivo que deseja abrir: ")
            with open(nome_arquivo, 'r') as arquivo:
                conteudo = arquivo.read()
                print("Conteúdo do arquivo:")
                print(conteudo)
                break
        except FileNotFoundError:
            print("Arquivo não encontrado. Verifique o nome e tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")


abrir_arquivo()


# Atividade 10


def raiz_quadrada_segura():
    while True:
        try:
            numero = float(
                input("Digite um número para calcular a raiz quadrada: "))
            if numero < 0:
                raise ValueError(
                    "Não é possível calcular a raiz quadrada de um número negativo.")
            raiz = math.sqrt(numero)
            print(f"A raiz quadrada de {numero} é {raiz:.2f}")
            break
        except ValueError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")


raiz_quadrada_segura()


# Atividade 11

def cadastro_aluno():
    while True:
        try:
            nome = input("Digite o nome do aluno: ")
            idade = int(input("Digite a idade do aluno: "))
            nota = float(input("Digite a nota final do aluno (0 a 10): "))

            if nota < 0 or nota > 10:
                print("Erro: A nota deve estar entre 0 e 10.")
                continue

            print("\nCadastro realizado com sucesso!")
            print(f"Nome: {nome}")
            print(f"Idade: {idade}")
            print(f"Nota final: {nota:.2f}")
            break
        except ValueError:
            print("Erro: Idade e nota devem ser valores numéricos. Tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")


cadastro_aluno()


# Atividade 12

def soma_com_finally():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        soma = num1 + num2
        print(f"A soma dos números é: {soma}")
    except ValueError:
        print("Erro: Por favor, insira apenas números válidos.")
    finally:
        print("Operação concluída.")


soma_com_finally()
