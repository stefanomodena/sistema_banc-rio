import textwrap

def menu():
    menu = """
    ========== MENU ==========
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [n] Nova conta
    [u] Novo usuário
    [l] Listar contas
    [q] Sair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso.")
    else:
        print("Valor inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite:
        print("Limite de saque excedido.")
    elif numero_saques >= limite_saques:
        print("Número máximo de saques atingido.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print("Saque realizado com sucesso.")
    else:
        print("Valor inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n========= EXTRATO =========")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for mov in extrato:
            print(mov)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("============================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (apenas números): ")
    if any(u["cpf"] == cpf for u in usuarios):
        print("Usuário já existe.")
        return
    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (rua, número - bairro - cidade/estado): ")
    usuarios.append({"nome": nome, "cpf": cpf, "nascimento": nascimento, "endereco": endereco})
    print("Usuário criado com sucesso.")

def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
    if usuario:
        contas.append({"agencia": agencia, "numero": numero_conta, "usuario": usuario})
        print("Conta criada com sucesso.")
    else:
        print("Usuário não encontrado.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência: {conta["agencia"]}
        Conta: {conta["numero"]}
        Titular: {conta["usuario"]["nome"]}
        """
        print("="*20)
        print(textwrap.dedent(linha))

# Programa principal
LIMITE_SAQUES = 3
AGENCIA = "0001"

saldo = 0
limite = 500
extrato = []
numero_saques = 0
usuarios = []
contas = []
numero_conta = 1

while True:
    opcao = menu()

    if opcao == "d":
        valor = float(input("Valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Valor do saque: "))
        saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )

    elif opcao == "e":
        exibir_extrato(saldo, extrato)

    elif opcao == "u":
        criar_usuario(usuarios)

    elif opcao == "n":
        criar_conta(AGENCIA, numero_conta, usuarios, contas)
        numero_conta += 1

    elif opcao == "l":
        listar_contas(contas)

    elif opcao == "q":
        break

    else:
        print("Opção inválida.")
