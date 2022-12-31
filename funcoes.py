# Exercícios com funções

# 1 - Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o valor total para uma variável e mostre o valor
# da variável

def multiplicator(*args):
    mult = 1
    for num in args:
        mult *= num

    return mult


result = multiplicator(1, 2, 3, 4)

print(result)


# 2 - Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar

def odd_or_even(num):
    result = 'Par' if num % 2 == 0 else 'Ímpar'

    return print(f"O número {num} é", result)


odd_or_even(6)
