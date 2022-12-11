'''
Faça um jogo para que o usuário adivinhar
qual a palavra secreta.

- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.

- Quando o usuário digitar a letra, você vai conferir se a letra digitada está na palavra secreta.

    - Se a letra digitada estiver na palavra secreta, exiba a letra;
    - Se a letra digitada não estiver na palavra secreta, exiba *.

Faça a contagem de tentativas do seu usuário.
'''
import os

secret = 'marsupial'
answers = ''
count = 0

os.system('clear')

while True:
    letter = input('Digite uma letra: ')
    count += 1

    if len(letter) > 1:
        print('Digite apenas uma letra.')
        continue

    if letter in secret:
        answers += letter

    formatted_word = ''
    for letter in secret:
        if letter in answers:
            formatted_word += letter
        else:
            formatted_word += '*'

    if formatted_word == secret:
        os.system('clear')
        print('Parabéns! Você ganhou! A palavra secreta foi:', secret.upper())
        print(f'Você fez {count} tentativas.')
        break
    else:
        print(formatted_word)

