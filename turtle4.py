########################################
##ANA LUISA RIGOTTI LEITE RA: 22400558##
########################################

########################################
##Felipe Rios dos Santos RA: 22403886###
########################################
from abc import ABC, abstractmethod

class ContaBancaria(ABC):
    def _init_(self, numero, titular, saldo=0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def calcular_saldo(self):
        pass

    def exibir_informacoes(self):
        print("\n---------------------")
        print(f"Conta Número: {self.numero}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: R${self.saldo:.2f}")
        print("---------------------\n")

class ContaCorrente(ContaBancaria):
    def _init_(self, numero, titular, saldo=0.0, limite_cheque_especial=500.0):
        super()._init_(numero, titular, saldo)
        self.limite_cheque_especial = limite_cheque_especial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and self.saldo - valor >= -self.limite_cheque_especial:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente para o saque com o limite de cheque especial.")

    def calcular_saldo(self):
        return self.saldo

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Limite Cheque Especial: R${self.limite_cheque_especial:.2f}")

class ContaPoupanca(ContaBancaria):
    def _init_(self, numero, titular, saldo=0.0, taxa_juros=0.01):
        super()._init_(numero, titular, saldo)
        self.taxa_juros = taxa_juros

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente. Operação não permitida em Conta Poupança.")

    def calcular_saldo(self):
        self.saldo += self.saldo * self.taxa_juros
        return self.saldo

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Taxa de Juros: {self.taxa_juros * 100:.2f}%")

def criar_conta_corrente():
    numero = input("Digite o número da conta corrente: ")
    titular = input("Digite o nome do titular da conta: ")
    saldo = float(input("Digite o saldo inicial: "))
    limite = float(input("Digite o limite do cheque especial: "))
    return ContaCorrente(numero, titular, saldo, limite)

def criar_conta_poupanca():
    numero = input("Digite o número da conta poupança: ")
    titular = input("Digite o nome do titular da conta: ")
    saldo = float(input("Digite o saldo inicial: "))
    taxa_juros = float(input("Digite a taxa de juros (ex.: 0.01 para 1%): "))
    return ContaPoupanca(numero, titular, saldo, taxa_juros)

if __name__ == "_main_":
    print("Bem-vindo ao sistema bancário!")
    tipo_conta = input("Digite o tipo de conta a ser criada (corrente/poupança): ").strip().lower()

    if tipo_conta == "corrente":
        conta = criar_conta_corrente()
    elif tipo_conta == "poupança":
        conta = criar_conta_poupanca()
    else:
        print("Tipo de conta inválido.")
        exit()

    conta.exibir_informacoes()

while True:
    print("\nOperações disponíveis: depositar, sacar, calcular saldo, exibir, sair")
    operacao = input("Escolha uma operação: ").strip().lower()

    match operacao:
        case "depositar":
            valor = float(input("Digite o valor a depositar: "))
            conta.depositar(valor)
        case "sacar":
            valor = float(input("Digite o valor a sacar: "))
            conta.sacar(valor)
        case "calcular saldo":
            saldo_atual = conta.calcular_saldo()
            print(f"Saldo atualizado: R${saldo_atual:.2f}")
        case "exibir":
            conta.exibir_informacoes()
        case "sair":
            print("Encerrando operações.")
            break
        case _:
            print("Operação inválida. Tente novamente.")