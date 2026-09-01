def gerar_tabuada():
    while True:
        print("\n--- Menu de Tabuada ---")
        print("Informe o número de 2 à 9")
        print("Ou 0 para Sair")

        escolha = input("\nEscolha uma opção (2-9): ")

        if escolha == '0':
            print("Encerrando o programa...")
            break
        
        numero = int(escolha)
        if numero >= 2 and numero <= 9:
            print(f"\nTabuada do {numero}:")
           
            for i in range(1, 11):
                resultado = numero * i
                print(f"{numero} x {i} = {resultado}")
        else:
            print("Opção inválida! Tente novamente.")
     
gerar_tabuada()