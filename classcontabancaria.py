class ContaBancaria:
    def __init__(self, titular: str, numero: int, nome_conta: str, tipo: str, numero_ficticio: int):
        self.titular = titular
        self.numero = numero
        self.nome_conta = nome_conta
        self.tipo = tipo
        self.numero_ficticio = numero_ficticio
        self.saldo = 0.0

    def depositar(self, valor: float):
        self.saldo += valor

    def sacar(self, valor: float):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")


conta1 = ContaBancaria("Maria laura", 105, "Conta Salário", "corrente", 1234567)

conta1.depositar(5000)

print("Saldo inicial: R$ 5000.00")
print("\n1 - Depositar")
print("2 - Sacar")
print("3 - Ver saldo")

opcao = input("Escolha: ")

if opcao == "1":
    valor = float(input("Valor: "))
    conta1.depositar(valor)
elif opcao == "2":
    valor = float(input("Valor: "))
    conta1.sacar(valor)
elif opcao == "3":
    print("Saldo:", conta1.saldo)
else:
    print("Opção inválida.")

print("\nEncerrando...")
print("Titular:", conta1.titular)
print("Conta:", conta1.nome_conta, "-", conta1.tipo)
print("Número fictício:", conta1.numero_ficticio)
print(f"Valor total na conta: R$ {conta1.saldo:.2f}")