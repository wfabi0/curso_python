# Atividade 13

primeiro_nome = input("Digite o seu primeiro nome: ")
sobrenome = input("Digite o seu sobrenome: ")

nome_completo = f"{primeiro_nome} {sobrenome}"

print("Nome completo em maiúsculas:", nome_completo.upper())
print("Nome completo em minúsculas:", nome_completo.lower())
print("Nome completo com a primeira letra de cada nome em maiúsculo:",
      nome_completo.title())


# Atividade 14

frase = input("Digite uma frase: ")

quantidade_a = frase.lower().count("a")
print(f"A letra 'a' aparece {quantidade_a} vezes na frase.")

quantidade_palavras = len(frase.split())
print(f"A frase contém {quantidade_palavras} palavras.")


# Atividade 15

texto = input("Digite uma palavra ou frase: ")

texto_invertido = texto[::-1]
print(f"O texto invertido é: {texto_invertido}")

# Atividade 16

palavra1 = input("Digite a primeira palavra: ").lower()
palavra2 = input("Digite a segunda palavra: ").lower()

if palavra1 == palavra2:
    print("As palavras são exatamente iguais.")
elif sorted(palavra1) == sorted(palavra2):
    print("As palavras são anagramas.")
else:
    print("As palavras são completamente diferentes.")


# Atividade 17

frase = input("Digite uma frase: ")

print("Frase original:", frase)

frase_substituida = frase.replace("Python", "Linguagem Python")
print("Frase após substituição:", frase_substituida)


# Atividade 18

frase = input("Digite uma frase: ")

palavras = frase.split()

print("Palavras separadas:")
for palavra in palavras:
    print(palavra)

print(f"Total de palavras digitadas: {len(palavras)}")
