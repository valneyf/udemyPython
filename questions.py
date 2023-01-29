# Exercício  - Sistema de perguntas e respostas

questions = [
    {
        'Question': 'Quanto é 2 + 2?',
        'Options': ['1', '3', '4', '5'],
        'Answer': '4',
    },
    {
        'Question': 'Quanto é 5 * 5?',
        'Options': ['25', '55', '10', '51'],
        'Answer': '25',
    },
    {
        'Question': 'Quanto é 10 / 2?',
        'Options': ['4', '5', '2', '1'],
        'Answer': '5',
    },
]

bingo_qty = 0
error_qty = 0

for question in questions:
    print('\nPergunta:', question['Question'], '\n')

    for i, option in enumerate(question['Options']):
        print(f'{i})', option)

    choice = input('\nEscolha uma opção: ')

    bingo = False
    int_choice = None
    if choice.isdigit():
        int_choice = int(choice)

    if int_choice is not None:
        if int_choice >= 0 and int_choice < len(question['Options']):
            if question['Options'][int_choice] == question['Answer']:
                bingo = True
                bingo_qty += 1

    print(f'\nVocê acertou {bingo_qty} de {len(questions)} perguntas')
