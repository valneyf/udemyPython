'''
Exercício - Salvar uma classe em JSON

Salvar os dados da classe em JSON
depois ciar novamente as instancias
da classe com os dados salvos
Criar arquivos separados para
- salvar a classe em JSON
- recuperar os dados em JSON
'''
import json

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'
    
    def to_json(self, file):
        with open(file, 'w') as output:
            return json.dump(self.__dict__, output, indent=2)
        
    def read_json(self, file):
        with open(file, 'r') as input:
            return print(json.load(input))
        
def create_json(db, file):
    with open(file, 'w') as input:
        print('Creating file JSON...')
        json.dump(db, input, indent=2)

def back_to_class(file):
    with open(file, 'r') as input:
        persons = json.load(input)

        for i, _ in enumerate(persons):
            p = Person(**persons[i])
            print(f'# {i} - {p}')
        
        print(f'Got {i + 1} persons')

p1 = Person('Marcos', 27)
p2 = Person('Ana', 35)
p3 = Person('Laura', 56)

print(p1)

db = [vars(p1), vars(p2), vars(p3)]

create_json(db, 'Persons.json')
back_to_class('Persons.json')

# print(vars(p1))
# p1.to_json('Person1.json')
# p1.read_json('Person1.json')