'''
Exercicio com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que 
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Cliente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrent que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (superclasse) deve ter o método sacar abstrato (Abstração e
    polimosfismo - as subclasses que implementam o método sacar)
Criar classe banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se o cliente é daquele banco
    * Checar se a agência é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método
'''

from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, agency, account_number, balance):
        self._agency = agency
        self._account_number = account_number
        self._balance = balance
        self._valid = False

    @property
    def valid(self):
        return self._valid
    
    @valid.setter
    @abstractmethod
    def valid(self, value): ...        

    @abstractmethod
    def deposit(self, value): ...

    @abstractmethod
    def withdraw(self, value):...

    def __str__(self) -> str:
        return f'Agencia: {self._agency}, Num. Conta: {self._account_number}, Saldo: R$ {self._balance:.2f}'

class CheckingAccount(Account):
    def __init__(self, agency, account_number, balance, additional_limit):
        super().__init__(agency, account_number, balance)
        self._additional_limit = additional_limit

    @property
    def additional_limit(self):
        return self._additional_limit
    
    @additional_limit.setter
    def additional_limit(self, additional_limit):
        self._additional_limit = additional_limit

    @Account.valid.setter
    def valid(self, value):
        self._valid = value
    
    def deposit(self, value): 
        self._balance += value
        print(f'Depósito realizado com sucesso!')

    def withdraw(self, value):
        if self.valid:
            if self._balance + self.additional_limit > 0 and (self._balance + self.additional_limit) - value >= 0:
                self._balance -= value
                print(f'Saque realizado com sucesso! Seu novo saldo é R$ {self._balance:.2f}')
            else:
                print(f'Saldo insuficiente')
        else:
            print('Operação não permitida.')    

    def __str__(self) -> str:
        return f'{super().__str__()}, Limite Extra: R$ {self.additional_limit:.2f}'

class SavingAccount(Account):
    def __init__(self, agency, account_number, balance):
        super().__init__(agency, account_number, balance)

    def deposit(self, value): 
        self._balance += value
        print(f'Depósito realizado com sucesso!')

    @Account.valid.setter
    def valid(self, value):
        self._valid = value

    def withdraw(self, value):
        if self.valid:
            if self._balance > 0 and self._balance - value >= 0:
                self._balance -= value
                print(f'Saque realizado com sucesso! Seu novo saldo é R$ {self._balance:.2f}')
            else:
                print(f'Saldo insuficiente')
        else:
            print('Operação não permitida.')

class Person(ABC):
    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age
    
    @property
    def name(self): 
        return self._name

    @name.setter
    def name(self, name): 
        self._name = name

    @property
    def age(self): 
        return self._age

    @age.setter
    def age(self, age): 
        self._age = age

    def __str__(self):
        return f'{self.name}, {self.age}'

class Client(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self._account = ''

    @property
    def account(self):
        return self._account
    
    @account.setter
    def account(self, account):
        self._account = account

    def __str__(self):
        return f'Cliente: {self.name}, {self.age}, Conta: {self.account}'

class Bank:
    def __init__(self):
        self._clients = []
        self._accounts = []
    
    def insert_clients(self, *clients):
        self._clients.extend(clients)
        
    def insert_accounts(self, *accounts):
        self._accounts.extend(accounts)

    def authentication(self, client, agency, account_number):
        c_authenticated = False
        a_authenticated = False
        account = None
        
        for c in self._clients:
            if c.name == client:
                c_authenticated = True
            
        for a in self._accounts:
            if a._agency == agency and a._account_number == account_number:
                account = a
                a_authenticated = True
        
        if c_authenticated and a_authenticated:
            print('Cliente autenticado.')
            account.valid = True
            return True
        else:
            print('Cliente, Agencia ou Conta informadas não pertencem a este banco')
            return False

checking_account = CheckingAccount('0123', 'x-0123', 120, 100)
print(checking_account)

saving_account = SavingAccount('0456', 'x-0456', 200)
print(saving_account)

valney = Client('Valney', 35)
valney.account = checking_account

bruna = Client('Bruna', 34)
bruna.account = saving_account
print(bruna)

banco1 = Bank()
banco1.insert_clients(valney, bruna)
banco1.insert_accounts(checking_account, saving_account)
banco1.authentication('Valney', '0123', 'x-0123')
banco1.authentication('Bruna', '0456', 'x-0456')

valney.account.withdraw(100)
bruna.account.withdraw(100)
print(checking_account)
print(saving_account)