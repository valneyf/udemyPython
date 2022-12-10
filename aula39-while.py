'''
Calculadora com while
'''
while True:
    num_1 = input('Digite o primeiro número: ')
    num_2 = input('Digite o segundo número: ')
    operator = input('Digite o operador [+-/*]:')

    invalid_number = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        invalid_number = True
    except:
        invalid_number = None

    if invalid_number is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    allowed_operators = '+-/*'

    if operator not in allowed_operators:
        print('Operador inválido.')
        continue

    if len(operator) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua operação. Confira o resultado abaixo:')

    if operator == '+':
        print(f'{num_1_float} + {num_2_float} =', num_1_float + num_2_float)

    if operator == '-':
        print(f'{num_1_float} - {num_2_float} =', num_1_float - num_2_float)

    if operator == '/':
        print(f'{num_1_float} / {num_2_float} =', num_1_float / num_2_float)

    if operator == '*':
        print(f'{num_1_float} * {num_2_float} =', num_1_float * num_2_float)

    sair = input('Deseja sair [s]im: ').lower().startswith('s')

    if sair is True:
        break

