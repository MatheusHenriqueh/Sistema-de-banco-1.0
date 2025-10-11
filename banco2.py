#Projeto de Banco
#Matheus Ruivo
#Data: 11/10/2025
#Treino para if, else e elif


print("Seja bem-vindo(a) ao banco!")
nome = input("Digite seu nome:")
senha = input("Digite sua senha:")
print("Carregando...")
print(f"Seja bem-vindo(a) de volta {nome}!")
saldo = float(input("Quanto de saldo tem na sua conta atualmente?"))
entrada = input("Quer entrar no banco? digite: entrar, se quiser sair digite: sair:")

if entrada == "entrar":
    print("Você entrou no painel do banco!")
    print(f"{nome}, você quer efetuar qual? pix, saque ou deposito?")
    pix = input("se quiser fazer pix, digite: pix:")
    if pix == "pix":
        print("Carregando..")
        pix1 = float(input(f"{nome}, qual número pretende fazer o pix?"))
        pix2 = float(input("Qual o valor que deseja?"))
        soma = saldo >= pix2
        if saldo >= pix2:
           saldo -= pix2  # desconta o valor do saldo
           print("✅ PIX ENVIADO COM SUCESSO!")
           print(f"💰 Valor enviado: R${pix2:.2f}")
           print(f"Saldo atual: R${saldo:.2f}")
        else:
           print("❌ Saldo insuficiente, tente de novo!")
    
    saque = input(f"{nome}, se quiser fazer saque, digite: saque:")
    if saque == "saque":
        print("Carregando..")
        saque1 = float(input("Quanto de dinheiro você quer sacar?"))
        soma1 = saldo >= saque1
        if saldo>= saque1:
           saldo -= saque1
           print("SAQUE DEU SUCESSO!")
           print(f"Valor do saque: {saque1:.2f}")
           print(f"Saldo atual: {saldo:.2f}")
        else:
            print("Saldo insuficiente, volte depois.")
    deposito = input(f"{nome}, se quiser fazer depósito digite: deposito:")
    if deposito == "deposito":
           print("Carregando sistema....")
           deposito1 = float(input("Qual o valor que deseja depositar?"))
           soma4 = saldo >= deposito1
           if saldo >= deposito1:
              saldo -= deposito1
              print("Depósito com sucesso!")
              print(f"Valor do depósito: {deposito1:.2f}")
              print(f"Valor do saldo atual: {saldo:.2f}")
           else:
               print("Saldo insuficiente, volte depois! ")  
elif entrada == "sair":
    print("Você saiu do sistema do banco!")
else:
    print("Você não digitou nem sair e nem entrar!")    