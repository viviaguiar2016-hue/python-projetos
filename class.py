import random
import string

class Carro:
    def __init__(self, modelo, ano, codigo):
        self.modelo = modelo
        self.ano = ano
        self.codigo = codigo

    def exibir_info(self):
        print(f"Modelo: {self.modelo}, Ano: {self.ano}, Código: {self.codigo}")


def gerar_codigo_aleatorio():
    letras = ''.join(random.choices(string.ascii_uppercase, k=3))
    numeros = ''.join(random.choices(string.digits, k=3))
    return letras + numeros


carros = []
quantidade = int(input("Quantos carros deseja cadastrar? "))

for i in range(quantidade):
    modelo = input(f"Digite o modelo do carro {i + 1}: ")
    ano = int(input(f"Digite o ano do carro {i + 1}: "))
    codigo = gerar_codigo_aleatorio()
    
    carro = Carro(modelo, ano, codigo)
    carros.append(carro)

print("\n--- Carros cadastrados ---")
for carro in carros:
    carro.exibir_info()