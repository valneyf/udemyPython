"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os

os.system('clear')

shopping_list = []
while True:
    print("Selecione uma opção")
    answer = input("[i]nserir [a]pagar [l]istar: ")
    
    if answer == 'i':
        os.system('clear')
        value = input('Valor: ')
        shopping_list.append(value)

    elif answer == 'a':
        index_answer = input('Informe o índice a ser removido: ')

        try:
            index = int(index_answer)
            del shopping_list[index]
        except:
            print('Não foi possível apagar este índice')

    elif answer == 'l':
        os.system('clear')

        if len(shopping_list) == 0:
            print('Nada para listar')       
        
        for idx, value in enumerate(shopping_list):
            print(idx, value)
