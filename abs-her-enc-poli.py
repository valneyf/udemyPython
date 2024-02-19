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
    def __init__(self, agency: str, account_number: str, balance: float = 0):
        self.agency = agency
        self.account_number = account_number
        self.balance = balance
        self._valid = False

    @abstractmethod
    def withdraw(self, value): ...

    @property
    def valid(self):
        return self._valid

    @valid.setter
    def valid(self, value):
        self._valid = value

    def deposit(self, value):
        self.balance += value
        self.details(f'DEPÓSITO R$ {value:.2f}')

    def details(self, msg=''):
        print(f'Seu saldo é: R$ {self.balance:.2f} ({msg})')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agency!r}, {self.account_number!r}, '\
            f'R$ {self.balance:.2f})'
        return f'{class_name}{attrs}'


class CheckingAccount(Account):
    def __init__(self, agency: str, account_number: str, balance: float = 0,
                 additional_limit: float = 0):
        super().__init__(agency, account_number, balance)
        self._additional_limit = additional_limit

    @property
    def additional_limit(self):
        return self._additional_limit

    @additional_limit.setter
    def additional_limit(self, additional_limit):
        self._additional_limit = additional_limit

    def withdraw(self, value):
        if self.valid:
            if self.balance + self.additional_limit > 0 and \
                    (self.balance + self.additional_limit) - value >= 0:
                self.balance -= value
                self.details(f'SAQUE R$ {value:.2f}')
                return self.balance
            else:
                print('Saldo insuficiente')
                self.details(f'SAQUE NEGADO R$ {value:.2f}')
        else:
            print('Operação não permitida. Favor efetuar autenticação')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agency!r}, {self.account_number!r}, '\
            f'R$ {self.balance:.2f}, R$ {self.additional_limit:.2f})'
        return f'{class_name}{attrs}'


class SavingAccount(Account):
    def withdraw(self, value):
        if self.valid:
            if self.balance > 0 and self.balance - value >= 0:
                self.balance -= value
                self.details(f'SAQUE R$ {value:.2f}')
                return self.balance
            else:
                print('Saldo insuficiente')
                self.details(f'SAQUE NEGADO R$ {value:.2f}')
        else:
            print('Operação não permitida. Favor efetuar autenticação')


class Person:
    def __init__(self, name: str, age: int) -> None:
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

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.name!r}, {self.age!r})'
        return f'{class_name}{attrs}'


class Client(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.account: Account | None = None


class Bank:
    def __init__(
            self,
            agencies: list[str] | None = None,
            clients: list[Person] | None = None,
            accounts: list[Account] | None = None):
        self.agencies = agencies or []
        self.clients = clients or []
        self.accounts = accounts or []

    def agency_checker(self, account):
        if account.agency in self.agencies:
            return True
        return False

    def client_checker(self, client):
        if client in self.clients:
            return True
        return False

    def account_checker(self, account):
        if account in self.accounts:
            return True
        return False

    def account_client_checker(self, client, account):
        if account is client.account:
            return True
        return False

    def authentication(self, client: Person, account: Account):
        if self.agency_checker(account) and \
                self.client_checker(client) and \
                self.account_checker(account) and \
                self.account_client_checker(client, account):
            account.valid = True
            print('Cliente autenticado.')

            return True
        else:
            print('Cliente, Agencia ou Conta não pertencem a este banco')
            return False

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencies!r}, {self.clients!r}, {self.accounts!r})'
        return f'{class_name}{attrs}'


checking_account = CheckingAccount('0123', 'x-0123')
# print(checking_account)

saving_account = SavingAccount('0456', 'x-0456', 200)
# print(saving_account)

valney = Client('Valney', 35)
valney.account = checking_account

bruna = Client('Bruna', 34)
bruna.account = saving_account
print(bruna)

banco = Bank()
print(banco)

banco.clients.extend([valney, bruna])
banco.accounts.extend([checking_account, saving_account])
banco.agencies.extend(['0123', '0456'])

print(banco)
# banco.insert_clients(valney, bruna)
# banco.insert_accounts(checking_account, saving_account)
banco.authentication(valney, checking_account)
# banco.authentication('Bruna', '0456', 'x-0456')

valney.account.withdraw(100)
valney.account.deposit(100)
valney.account.withdraw(100)
bruna.account.withdraw(100)
bruna.account.deposit(100)
print(checking_account)
print(saving_account)
