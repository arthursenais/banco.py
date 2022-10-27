import os
os.system("cls")
global saldo
global logado
saldo = 25000.23
logado = False
def login():
    global logado
    print("Insira o cartão do banco ou digite o número da agência e conta")
    for i in range(100):
        print("digite o número da agência")
        n_agencia = input("--->")
        if len(n_agencia) < 4:
            print("nº da agência deve ter mais que 4 dígitos e não pode ser nulo")
        else:
            break
    for i in range(100):
        print("Digite o número da conta:")
        n_conta = input("--->")
        if len(n_conta) != 10:
            print("nº da conta deve ter 10 dígitos")
        else:
            break
    n_tentativas = 0
    for i in range(4):
        print("Por favor digite sua senha:")
        n_senha = int(input("--->"))
        n_tentativas += 1
        if n_senha == 1234:
            print("Acesso autorizado")
            break
        else:
            print("Senha incorreta.")
    if n_tentativas >= 4:
        print("Acesso bloqueado")
    else:
        logado = True
        sacar()

def sacar():
    global saldo
    print(f"Saldo: R${saldo}")
    for i in range(100):
        print("Digite o valor a ser sacado:")
        v_sacado = float(input("--->"))
        if v_sacado < 0 or v_sacado > saldo:
            print("Valor inválido ou saldo insuficiente\n[0] Sair\n[1] Sacar outro valor\n")
            opcao = int(input("--->"))
            if opcao == 0:
                return 0;
            elif opcao == 1:
                sacar()
        else:
            saldo -= v_sacado
            print("Operação realizada")   
            main()
            break

def main():
    print("----------")
    print("Bem vindo")
    if logado == True:
        print(f"Saldo: R${saldo}")
    print("----------")
    print("[0] Sair")
    print("[1] Sacar dinheiro")
    selecionado = int(input("\n--->"))
    if selecionado == 0:
       return 0;
    elif selecionado == 1:
        if logado == True:
            sacar()
        elif logado == False:
            login()
main()