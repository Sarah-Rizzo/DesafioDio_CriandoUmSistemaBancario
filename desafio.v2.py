menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=>"""

saldo = 0
deposito = 0
extrato = ""
saque = 0
LIMITE_MAXIMO = 500
numero_de_saques = 0







while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor:"))

        if valor > 0:
            saldo += valor
            

    elif opcao == "2":
        valor = float(input("Informe o valor que deseja sacar:"))
        

        if valor <= saldo and numero_de_saques <=3:
            saldo -= valor
            numero_de_saques += 1

            


        else:
            print("Valor não autorizado, seu saldo é insuficiente.")

    elif opcao == "3":
        print(f"Seu saldo é: R$ {saldo:.2f}")
        print(f"\nVocê realizou: {numero_de_saques} saques.")     

    elif opcao == "0":
        print("Operação finalizada")
        break

    else:
        print("Informe uma opção valida:")           
            
    








