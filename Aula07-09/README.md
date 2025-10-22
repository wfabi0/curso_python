# Aula 07-09 - Exercícios de Estruturas de Dados em Python

## 📚 Lista de Exercícios

## LISTAS

1. Escreva um algoritmo que armazene em um vetor (lista) todos os números inteiros de 1 a 50 e, em seguida, imprima todos os valores armazenados.
2. Escreva um algoritmo que armazene em um vetor todos os números inteiros de 100 a 1 (em ordem decrescente) e, em seguida, imprima todos os valores armazenados.
3. Escreva um algoritmo que armazene em um vetor os 100 primeiros números ímpares e, em seguida, imprima todos os valores armazenados.
4. Escreva um algoritmo que leia 10 números e armazene em um vetor a metade de cada número. Depois, exiba todos os valores armazenados.
5. Escreva um algoritmo que leia 10 números e armazene em um vetor o quadrado de cada número. Depois, exiba todos os valores armazenados.
6. Escreva um programa que leia 6 números inteiros representando o gabarito da Mega Sena e, em seguida, leia 10 apostas com 6 números cada. O programa deve informar quantos acertos cada apostador obteve e se fez quadra (4 acertos), quina (5 acertos) ou sena (6 acertos).

---

## MATRIZES

1. Faça um programa que leia uma matriz 2x2 de números inteiros e exiba todos os valores na tela.
2. Faça um programa que leia uma matriz 3x3 de números inteiros e imprima o conteúdo organizado em forma de tabela.
3. Escreva um algoritmo que leia uma matriz 3x3 e exiba a soma dos elementos de cada linha.
4. Escreva um algoritmo que leia uma matriz 3x3 e exiba a soma dos elementos de cada coluna.
5. Faça um programa que calcule a soma das diagonais principal e secundária de uma matriz 3x3.
6. Faça um programa que verifique se uma matriz 3x3 forma um quadrado mágico (ou seja, se as somas das linhas, colunas e diagonais são iguais).
7. Escreva um programa que leia uma matriz 2x3 de Strings (nomes ou letras) e exiba seu conteúdo.
8. Crie um programa que leia uma matriz 2x2 de números reais e exiba seus valores.
9. Realize a soma das duas matrizes 2x2 e exiba o resultado.
10. Realize a multiplicação das duas matrizes 2x2 e exiba o resultado.

---

## TUPLAS

1. Crie uma tupla com os números de 1 a 5 e exiba todos os seus elementos na tela.
2. Crie uma tupla com os nomes de cinco cidades brasileiras e exiba apenas a primeira e a última cidade da tupla.
3. Crie uma tupla com dez números inteiros.
   - Mostre o menor e o maior número da tupla.
   - Mostre também a quantidade de elementos usando `len()`.
4. Crie duas tuplas com números inteiros e gere uma nova tupla resultante da soma (concatenação) das duas.
5. Crie uma tupla com quatro elementos e repita-a três vezes usando o operador `*`.
6. Crie uma tupla com os elementos (5, 10, 15, 10, 20, 10) e:
   - Conte quantas vezes o número 10 aparece (`count()`).
   - Mostre o índice da primeira ocorrência do número 15 (`index()`).
7. Crie uma tupla com os valores (10, 20, 30) e use desempacotamento para atribuir cada valor a uma variável diferente (`a`, `b`, `c`). Depois, exiba as três variáveis separadamente.
8. Crie uma tupla aninhada, representando as notas de três alunos, sendo cada tupla interna as três notas do aluno. Exemplo: `((7,8,6), (9,5,7), (8,8,10))` Mostre a primeira nota do segundo aluno e a média do terceiro aluno.

---

## CONJUNTOS

1. Crie um conjunto com os elementos `'maçã'`, `'banana'`, `'uva'`, `'maçã'` e exiba o conjunto. (Observe o que acontece com o elemento repetido.)
2. Crie dois conjuntos: `a={1,2,3,4,5}` e `b={4,5,6,7,8}`
   - Mostre:
     - A união dos dois conjuntos.
     - A interseção dos dois conjuntos.
     - A diferença entre `a` e `b`.
3. Crie um conjunto com os números pares de 0 a 10 e verifique se o número 6 pertence a ele.
4. Crie um conjunto vazio e adicione três nomes de alunos usando o comando `add()`. Em seguida, remova um nome com `remove()` e exiba o conjunto atualizado.
5. Crie um conjunto com letras do alfabeto (`{'a','b','c','d'}`) e use um laço `for` para imprimir cada elemento do conjunto.
6. Crie um conjunto com os números `{1,2,3}` e outro `{3,4,5}`. Exiba:
   - A união (`|`)
   - A interseção (`&`)
   - A diferença simétrica (`^`)

---

## DICIONÁRIOS (Dict)

1. Crie um dicionário com as chaves `nome`, `idade` e `cidade`, e preencha com seus próprios dados. Depois, exiba apenas o valor associado à chave `nome`.
2. Crie um dicionário com três alunos, onde a chave é o nome e o valor é a nota. Exemplo: `alunos = {'Ana':8.5, 'Bruno':7.0, 'Carlos':9.2}` Exiba apenas os nomes dos alunos (`keys()`) e depois apenas as notas (`values()`).
3. Crie um dicionário e adicione duas novas chaves manualmente. Em seguida, altere o valor de uma das chaves e exiba o dicionário atualizado.
4. Crie um dicionário representando um produto com as chaves: `nome`, `preço`, `estoque`.
   - Exiba o nome e o preço formatado (R$).
   - Aumente o estoque em +5 unidades e mostre o dicionário atualizado.
5. Crie um dicionário aninhado que armazene dois alunos, cada um com suas notas. Exemplo:
   ```python
   alunos = {
       "João": {"nota1": 8, "nota2": 7},
       "Maria": {"nota1": 9, "nota2": 10}
   }
   ```
   Exiba a `nota2` de Maria.
6. Crie uma lista de tuplas com pares de chave-valor, por exemplo: `[("nome","Carlos"), ("idade",25), ("cidade","Contagem")]` Converta essa lista em um dicionário usando `dict()` e exiba o resultado.
7. Crie um dicionário que guarde os nomes de 3 alunos e seus conjuntos de disciplinas. Exemplo:
   ```python
   alunos = {
       "Ana": {"Matemática", "Física"},
       "Bruno": {"Geografia", "História"},
       "Carla": {"Matemática", "História"}
   }
   ```
   Mostre todas as disciplinas cursadas por Ana e Carla (união dos conjuntos).
8. Crie uma tupla com números de 1 a 10, converta-a para lista, adicione o número 11, e depois converta novamente para tupla. Exiba o resultado final.
9. Crie uma lista de nomes com repetições e converta-a em um conjunto para eliminar duplicatas. Exiba a lista original e o conjunto resultante.
10. Crie um dicionário onde as chaves são os números de 1 a 5 e os valores são seus quadrados. Exemplo: `{1:1, 2:4, 3:9, ...}` Exiba o dicionário completo.
