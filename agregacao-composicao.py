'''
Exercício com classes
1 - Criar uma classe Carro (Nome) ok
2 - Criar uma classe Motor (Nome) ok
3 - Criar uma classe Fabricante (Nome) ok
4 - Criar uma ligação entre Carro tem um Motor
OBS: Um motor pode ser de vários carros
5 - Criar uma ligação entre Carro e Fabricante
OBS: Um fabricante pode fabricar vários carros

Exibir o nome do carro, motor e fabricante na tela
'''

class Car():
    def __init__(self, name):
        self.name = name
        self.engine = None
        self.manufacturer = None

    def set_engine(self, motor):
        self.engine = motor.name

    def set_manufacturer(self, vendor):
        self.manufacturer = vendor.name

    def __str__(self):
        return f'Carro: {self.name}, Motor: {self.engine}, Fabricante: {self.manufacturer}'

class Engine():
    def __init__(self, name):
        self.name = name

class Manufacturer():
    def __init__(self, name):
        self.name = name

car1 = Car('Palio')

engine1 = Engine('CVT 1.4')
car1.set_engine(engine1)

manufacturer1 = Manufacturer('Fiat')
car1.set_manufacturer(manufacturer1)

print(car1)