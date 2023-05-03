# List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis

# print(list(range(10)))
# lista = []
# for numero in range(10):
#     lista.append(numero)
# print(lista)

# lista = [numero * 2 for numero in range(10)]
# print(lista)

# Mapeamento de dados em list comprehension
# No mapeamento, valores ternários, ifs e etc
# são colocados antes do for no comprehension list
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

# Mapeia todos os produtos, aumentando
# valores de preço em 5%
# novos_produtos = [
#     {**produto, 'preco': produto['preco'] * 1.05}
#     for produto in produtos
# ]

# Mapeia valores de preço maiores de 20
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}  # Ternario antes do for
    for produto in produtos
]

print(*novos_produtos, sep='\n')
