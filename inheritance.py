"""
Herança simples - Relações entre classes
Associação - Usa
Agregação - Tem
Composição - É dono de
Herança - É um

Herança ou Composição

Classe principal (Person)
-> super class, base class, parent class

Classes filhas (Client)
-> sub class, child class, derivad class
"""

# Super class
class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
    
    def class_name_indicator(self):
        print(self.name, self.last_name, self.__class__.__name__)

# Child class (A herança acontece com o '(nome_da_super_classe)')
    # Aqui a classe herda de 'Person' 
class Client(Person):
    ...

# Child class
class Student(Person):
    ...


p1 = Client('Valney', 'Filho')
p1.class_name_indicator()

s1 = Student('Bruna', 'Siqueira')
s1.class_name_indicator()