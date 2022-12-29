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

--------------------------------------------------------------

Cálculo do segundo dígito para CPF

CPF: 429.905.440-70
COlete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DÍGITO,
multiplicando cada um dos valores por uma 
contagem regressiva começando de 11

Ex.: 429.905.440-70 (4299054407)
   11 10  9  8  7  6  5  4  3  2
*  4  2   9  9  0  5  4  4  0  7 <-- PRIMEIRO DÍGITO
   44 20  81 72 0  30 20 16 0  14

Somar todos os resultados:
    44+20+81+72+0+30+20+16+0+14 = 297
Multiplicar o resultado anterior por 10
    297 * 10 = 2970
Obter o resto da divisão da conta anterior por 11
    2970 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
import random

def main():       
    cpf_generate = ""

    for i in range(9):
        cpf_generate += str(random.randint(0, 9))

    # Cálculo do primeiro dígito
    digit_one = digit_calculator(cpf_generate, 1)

    # Cálculo do segundo dígito
    digit_two = digit_calculator(cpf_generate + digit_one, 2)

    cpf_full = cpf_generate + digit_one + digit_two

    print("\n O CPF gerado foi: ", '{}.{}.{}-{}'.format(cpf_full[:3], cpf_full[3:6], cpf_full[6:9], cpf_full[9:]))

    print("\n Obrigado por utilizar nosso gerador de CPF")


def digit_calculator(cpf, position):
    # Cálculo do dígito
    digit_Sum = 0

    aux = 9 if position == 1 else 10

    for num in range(aux):
        digit_Sum += int(cpf[num]) * (aux + 1 - num)

    digit = (digit_Sum * 10) % 11

    digit = 0 if digit > 9 else digit

    return str(digit)

if __name__ == '__main__':
    main()