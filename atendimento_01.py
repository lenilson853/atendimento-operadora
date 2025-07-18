import time 

menu="""
Olá seja bem-vindo ao nosso atendimento!

[1]: Saldo
[2]: Recarga
[3]: Promoções
[4]: Internet
[5]: Outros serviços 
[0]: Encerrar atendimento
"""

saldo=0

while True:

    opcao=input(menu)

    if opcao == "1":
        print("Seu saldo é R$ {:.2f} ".format(saldo))

    elif opcao=="2":
        
            print("Valores disponíveis:")
            print("[1] R$10 ")
            print("[2] R$20 ")
            print("[3] R$30 ")
            print("[4] R$40 ")
            print("[5] Sair ")

            recarga_opcao= input("Escolha uma opção de recarga.")

            if recarga_opcao=="1":
            
                saldo+=10
                print("Recarga de R$10 realizada com sucesso.")
                print("Obrigado volte sempre!")

            elif recarga_opcao=="2":
                    saldo+=20
                    print("Recarga de R$20 realizada com sucesso.")
                    print("Obrigado volte sempre!")

            elif recarga_opcao=="3":
                    saldo+=30
                    print("Recarga de R$30 realizada com sucesso.")
                    print("Obrigado volte sempre!")

            elif recarga_opcao=="4":
                    saldo+=40
                    print("Recarga de R$40 realizada com sucesso.")
                    print("Obrigado, volte sempre!")
            elif recarga_opcao=="5":
                    print("Voltando ao menu...")
                    time.sleep(2)
                    
            else:
                    print("Opção inválida!")

    elif opcao=="3":
        print("\n[1]Internet em Dobro: Ative 3GB e ganhe 3GB extras.")
        print("\n[2]Ligações Ilimitadas para qualquer operadora por 30 dias.")
        print("\n[3]voltar ao menu principal.")

        opcao_promocao=input("Digite opção desejada!")

        if opcao_promocao=="1":
            print("\nPromoção ativada com sucesso, obrigada!")

        elif opcao_promocao=="2":
               print("\nPromoção ativada com sucesso!")

            
    elif opcao=="4":
        print("[1] 1GB por R$9,99")
        print("[2] 3GB por R$19,99")

        opcao_internet=input("Digite a opção desejada!")

        if opcao_internet=="1":
              print("\nPacote ativado com sucesso!")
        elif opcao_internet=="2":
              print("Pacote ativado com sucesso!")
              

    elif opcao=="5":

        print("[1] Ativar roaming")
        print("[2] Atendimento com nosso atendente?!")

        opcao_servico=input("Digite a opção desejada!")
        
        if opcao_servico=="1":
            print("Seu roaming está ativado")

        elif opcao_servico=="2":
             
              print("Só um momento, aguarde...")
              time.sleep(3)
              print("\nEstamos transferindo seu atendimento")


    elif opcao == "0":
        print("👋 Obrigado por usar nosso atendimento. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
