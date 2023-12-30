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
        self._engine = None
        self._manufacturer = None

    @property
    def engine(self):
        return self._engine
    
    @engine.setter
    def engine(self, motor):
        self._engine = motor.name

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, vendor):
        self._manufacturer = vendor.name

    def __str__(self):
        return f'Carro: {self.name}, Motor: {self.engine}, Fabricante: {self.manufacturer}'

class Engine():
    def __init__(self, name):
        self.name = name

class Manufacturer():
    def __init__(self, name):
        self.name = name

'###############################'
palio = Car('Palio')
engine1 = Engine('Fire 1.4')
palio.engine = engine1
manufacturer1 = Manufacturer('Fiat')
palio.manufacturer = manufacturer1

print(palio)

uno = Car('Uno')
# engine1 = Engine('Fire 1.4')
uno.engine = engine1
# manufacturer1 = Manufacturer('Fiat')
uno.manufacturer = manufacturer1

print(uno)

