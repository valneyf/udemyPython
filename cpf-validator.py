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
import re

def main():    
    while True:    
        cpf_user = input("Digite um cpf para validar (Ex.: 429.905.440-70): ")

        cpf = re.sub(   # <-- regex com função sub, "Substituir"
            r'[^0-9]',  # <-- expressão regular verifica tudo que não é número de 0 a 9
            '',         # <-- substitui tudo que a regex encontrar por nada ""
            cpf_user    # <-- dado que será aplicado a regex 
        )

        if len(cpf) != 11 or cpf == cpf[0] * len(cpf):
            print("\n Favor inserir cpf válido.")
            break

        # Cálculo do primeiro dígito
        digit_one = digit_calculator(cpf, 1)

        print("\n O primeiro dígito do CPF informado é: ", digit_one)

        # Cálculo do segundo dígito
        digit_two = digit_calculator(cpf, 2)

        print("\n O segundo dígito do CPF informado é: ", digit_two)

        cpf_gerado = cpf[:9] + str(digit_one) + str(digit_two)

        if cpf == cpf_gerado:
            print("\nCPF válido")
        else:
            print("\nCPF inválido...")

        break

    print("\n Obrigado por utilizar nosso validador de CPF")


def digit_calculator(cpf, position):
    # Cálculo do dígito
    digit_Sum = 0

    aux = 9 if position == 1 else 10

    for num in range(aux):
        digit_Sum += int(cpf[num]) * (aux + 1 - num)

    digit = (digit_Sum * 10) % 11

    digit = 0 if digit > 9 else digit

    return digit

if __name__ == '__main__':
    main()