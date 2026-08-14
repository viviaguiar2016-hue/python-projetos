import secrets
import string

# Criando nome para acesso de entrada de login
def login_acesso():
    print("******* Criando acesso Login *******")
    escolha = input("Escolha seu nome e sobrenome para acesso: ")
    return escolha

# Criando senha personalizada para usuario e fazendo tratamento de erro.
def senha_acesso():
    print("Criando senha da sua escolha")
    caracteres = string.ascii_letters + string.digits + string.punctuation

    try:
        tamanho = int(input("Escolha o tamanho da sua senha (mínimo 8 caracteres): "))
        if tamanho < 8:
            print("Digite no mínimo 8 caracteres para sua segurança")
            tamanho = 8
    except ValueError:
        print("Entrada inválida, digite um número")
        print("***** Usando tamanho padrão de 8 caracteres *****")
        tamanho = 8

    senha = "".join(secrets.choice(caracteres) for _ in range(tamanho))
    print("******* Sua senha foi gerada com sucesso: {} *******".format(senha))
  


if __name__ == "__main__":
    login_acesso()
    senha_acesso()