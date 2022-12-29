"""
Cálculo do primeiro dígito do CPF

CPF: 429.905.440-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.: 429.905.440-70 (429905440)
   10  9  8  7  6  5  4  3  2
*  4   2  9  9  0  5  4  4  0
   40  18 72 63 0  25 16 12 0

Somar todos os resultados:
    40+18+72+63+0+25+16+12+0 = 246
Multiplicar o resultado anterior por 10
    246 * 10 = 2460
Obter o resto da divisão da conta anterior por 11
    2460 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

# Cálculo do primeiro dígito
cpf = input("Digite um cpf para validar (Ex.: 42990544070): ")

if not cpf.isnumeric():
    print("Favor inserir somente números.")
    cpf = False

if len(cpf) != 11:
    print("Favor inserir cpf válido.")
    cpf = False

if cpf == True:
    digit_Sum = 0
    for num in range(9):
        print(num, '-', cpf[num], '10 - num = ', 10 - num)
        digit_Sum += int(cpf[num]) * (10 - num)
        print(digit_Sum)

    digit_one = (digit_Sum * 10) % 11

    if digit_one > 9:
        digit_one = 0

    print("O primeiro dígito do CPF informado é: ", digit_one)