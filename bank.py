'''
### Operações:

- Depósito: permite apenas valores inteiros e positivos. Os depositos devem ser exibidos na operação de extrato.
- Saque   : limite de 3 saques diários de até R$ 500,00 cada. Caso não haja saldo, exiba a mensagem: "Saldo insuficiente". 
            Os saques devem ser exibidos no extrato.
- Extrato : deve listar todos os depositos e saques. Além disso, deve exibir o saldo atual da conta no final da operação.
            Se o extrato estiver em branco, exibir a mensagem: "Não foram realizadas movimentações."
            
Nota: os valores devem ser exibidos utilizando o formato R$ xxx.xx. Exemplo 1500,45 = R$ 1500.45.
'''

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0

LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao != "d" and opcao != "s" and opcao != "e" and opcao != "q":
        print("Opção inválida!")
        break
    
    if opcao == "d":
        print("Depósito: ")
        valor = float(input("Valor do depósito: "))
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    
    if opcao == "s":
        print("Sacar: ")
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Valor do saque: "))
            if valor <= saldo and valor <= limite:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
            else:
                print("Saque inválido. Saldo insuficiente ou limite excedido.")
        else:
            print("Limite de saques diários atingido.")
    
    if opcao == "e":
        print("Extrato".center(28,"="))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("".center(28,"="))
        print("Saldo")
        print(f"{saldo:.2f}")
    
    if opcao == "q":
        print("Até logo!")
        break

print("Obrigado por usar nossos serviços!")