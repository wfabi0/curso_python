def q01():
    dados_pessoais = {
        'nome': 'João Silva',
        'idade': 28,
        'cidade': 'São Paulo'
    }
    print(dados_pessoais['nome'])


def q02():
    alunos = {
        'Ana': 8.5,
        'Bruno': 7.0,
        'Carlos': 9.2
    }
    print("Nomes dos alunos:", alunos.keys())
    print("Notas dos alunos:", alunos.values())


def q03():
    produto = {
        'nome': 'Notebook',
        'preço': 3500.00
    }
    produto['estoque'] = 50
    produto['marca'] = 'Dell'
    produto['preço'] = 3200.00
    print(produto)


def q04():
    produto = {
        'nome': 'Smartphone',
        'preço': 1500.00,
        'estoque': 30
    }
    print(f"Nome: {produto['nome']}, Preço: R$ {produto['preço']:.2f}")
    produto['estoque'] += 5
    print("Dicionário atualizado:", produto)


def q05():
    alunos = {
        "João": {"nota1": 8, "nota2": 7},
        "Maria": {"nota1": 9, "nota2": 10}
    }
    print("Nota2 de Maria:", alunos["Maria"]["nota2"])


def q06():
    lista_tuplas = [("nome", "Carlos"), ("idade", 25), ("cidade", "Contagem")]
    dicionario = dict(lista_tuplas)
    print(dicionario)


def q07():
    alunos = {
        "Ana": {"Matemática", "Física"},
        "Bruno": {"Geografia", "História"},
        "Carla": {"Matemática", "História"}
    }
    disciplinas_ana_carla = alunos["Ana"].union(alunos["Carla"])
    print("Disciplinas cursadas por Ana e Carla:", disciplinas_ana_carla)


def q08():
    nomes = ["Ana", "Bruno", "Carla", "Ana", "Bruno"]
    conjunto_nomes = set(nomes)
    print("Lista original:", nomes)
    print("Conjunto sem duplicatas:", conjunto_nomes)


def q09():
    quadrados = {}
    for i in range(1, 6):
        quadrados[i] = i**2
    print(quadrados)
