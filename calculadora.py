import time
import os

def limpar_tela():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def tela_splash():
    """Exibe a tela splash da calculadora."""
    limpar_tela()
    print("************************************")
    print("------------------------------------")
    print("*       Calculadora Simples        *")
    print("*        Criada em Python          *")
    print("*               Por                *")
    print(">>>>>>>    Douglas Lavina    <<<<<<<")
    print(">>>>>>>      Versão 1.0      <<<<<<<")
    print("------------------------------------")
    print("************************************")
    print("\nCarregando...")
    time.sleep(11)  # Pausa por 11 segundos
    limpar_tela()
# Exibe a tela splash antes do loop principal
tela_splash()
# Calculadora Simples
while True:
    while True:
        print()  # imprime uma linha em branco! Pulando uma linha!
        entrada_num1 = input("Digite o primeiro número: ")
        if entrada_num1.strip():
            try:
                num1 = int(entrada_num1)
                break
            except ValueError:
                print()  # imprime uma linha em branco! Pulando uma linha!
                print("Entrada inválida! Digite um número inteiro, por favor!")
        else:
            print()  # imprime uma linha em branco! Pulando uma linha!
            print("Entrada inválida! Nenhum número foi digitado! Digite um número, por favor!")

    while True:
        print()  # imprime uma linha em branco! Pulando uma linha!
        entrada_num2 = input("Digite o segundo número: ")
        if entrada_num2.strip():
            try:
                num2 = int(entrada_num2)
                break
            except ValueError:
                print()  # imprime uma linha em branco! Pulando uma linha!
                print("Entrada inválida! Digite um número inteiro, por favor!")
        else:
            print()  # imprime uma linha em branco! Pulando uma linha!
            print("Entrada inválida! Nenhum número foi digitado! Digite um número, por favor!")


    print()  # imprime uma linha em branco! Pulando uma linha!
    print("Escolha uma Operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair da Calculadora")

    while True:
        print()  # imprime uma linha em branco! Pulando uma linha!
        entrada_opcao = input("Digite o número da Operação: ")
        if entrada_opcao.strip():
            try:
                opcao = int(entrada_opcao)
                break
            except ValueError:
                print()  # imprime uma linha em branco! Pulando uma linha!
                print("Entrada inválida! Escolha o número da Operação de 1 a 5, por favor!")
                print("Lembrando: 1. Soma | 2. Subtrai | 3. Multiplica | 4. Divide | 5. Sai da Calculadora")
        else:
            print()  # imprime uma linha em branco! Pulando uma linha!
            print("Entrada inválida! Nenhum número foi digitado! Escolha o número da Operação de 1 a 5, por favor!")
            print("Lembrando: 1. Soma | 2. Subtrai | 3. Multiplica | 4. Divide | 5. Sai da Calculadora")
            
    if opcao == 1:
        resultado = num1 + num2
        print()  # imprime uma linha em branco! Pulando uma linha!
        print("O Resultado da soma é:", resultado)
    elif opcao == 2:
        resultado = num1 - num2
        print()  # imprime uma linha em branco! Pulando uma linha!
        print("O Resultado da subtração é:", resultado)
    elif opcao == 3:
        resultado = num1 * num2
        print()  # imprime uma linha em branco! Pulando uma linha!
        print("O Resultado da multiplicação é:", resultado)
    elif opcao == 4:
        if num2 == 0:
            print()  # imprime uma linha em branco! Pulando uma linha!
            print("Divisão por zero, aqui, NÃO É PERMITIDO!")
        else:
            resultado = num1 / num2
            print()  # imprime uma linha em branco! Pulando uma linha!
            print("O Resultado da divisão é:", resultado)
    elif opcao == 5:
        print()  # imprime uma linha em branco! Pulando uma linha!
        print("Calculadora encerrada com SUCESSO...")
        break
    else:
        print()  # imprime uma linha em branco! Pulando uma linha!
        print("Opção inválida! Reiniciando a calculadora!")
        


#
#
#   
#   >>>>>>>>> Projeto Calculadora Express <<<<<<<<<<<<<<<<<<<
#   >>>>>>>>>      Fim da Aplicação     <<<<<<<<<<<<<<<<<<<<<
#   >>>>>>>>>            2025           <<<<<<<<<<<<<<<<<<<<< 