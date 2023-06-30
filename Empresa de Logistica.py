#Inicio da função dimensoesObjeto()
def dimensoesObjeto(): #Definindo o nome da função
    while True: #Iniciando o laço (loop infinito)
        try: #Comando tenta executar a próxima linha sem erro
            altura = float(input('Digite a altura do objeto (em cm): ')) #Pedido para o usuário informação da altura
            comprimento = float(input('Digite o comprimento do objeto (em cm): ')) #Pedido para o usuário informação do comprimento
            largura = float(input('Digite a largura do objeto (em cm): ')) #Pedido para o usuário informação da largura
            dimensoesObjeto = altura * comprimento * largura #Fórmula para o cálculo da dimensão do produto a partir dos dados inseridos pelo usuário
            if dimensoesObjeto < 1000: #Caso o resultado do calculo de dimensõesObejto seja menor que 1000
                print('O volume do objeto é (em cm³): {:.2f}'.format(dimensoesObjeto)) #será exibido o resultado do calculo dimensoesObjeto
                return 10 #Valor que será considerado nesse caso
            elif dimensoesObjeto >= 1000 and dimensoesObjeto < 10000:
                print('O volume do objeto é (em cm³): {:.2f}'.format(dimensoesObjeto))
                return 20
            elif dimensoesObjeto >= 10000 and dimensoesObjeto < 30000:
                print('O volume do objeto é (em cm³): {:.2f}'.format(dimensoesObjeto))
                return 30
            elif dimensoesObjeto >=30000 and dimensoesObjeto < 100000:
                print('O volume do objeto é (em cm³): {:.2f}'.format(dimensoesObjeto))
                return 50
            elif dimensoesObjeto >= 100000: #Caso o resultado seja igual ou superior a 100000, não será aceito conforme print abaixo
                print('Não aceitamos objetos com dimensões tão grandes.')
                print('Entre com as dimensões desejadas novamente.')
                continue #Volta para o inicio do laço
        except ValueError: #Caso de erro na tentativa, vai retornar no console as frases abaixo
            print('Você digitou alguma dimensão do objeto com valor não numérico!')
            print('Por favor entre com as dimensões desejadas novamente.')
#Término da função dimensoesObjeto()

#Inicio da função pesoObjeto()
def pesoObjeto(): #Definindo o nome da função
    while True: #Iniciando o laço (loop infinito)
        try: #Comando tenta executar a próxima linha sem erro
            pesoObjeto = float(input('Digite o peso do objeto (em kg): ')) #Pedindo ao usuário a informação de peso
            if pesoObjeto < 0.1: #Caso peso seja menor que 0.1
                return 1 #Declarando o multiplicador referente ao peso menor que 0.1
            elif pesoObjeto >= 0.1 and pesoObjeto < 1:
                return 1.5
            elif pesoObjeto >= 1 and pesoObjeto < 10:
                return 2
            elif pesoObjeto >= 10 and pesoObjeto < 30:
                return 3
            else: #Caso o peso digitado não esteja entre os pesos declarados, será exibido no console as seguintes frases
                print('Não aceitamos objetos tão pesados.')
                print('Entre com o peso desejado novamente.')
                continue #Volta para o inicio do laço para que digite um valor valido
        except ValueError: #Caso de erro na tentativa, vai retornar no console as frases abaixo
            print('Você digitou peso do objeto com valor não numérico!')
            print('Por favor, entre com o peso desejado novamente.')
#Término da função pesoObjeto()

#Inicio da função rotaObjeto()
def rotaObjeto(): #Definindo o nome da função
    while True: #Iniciando o laço (loop infinito)
        rotaObjeto = input('Selecione a rota:\n'+
                           'RS - De Rio de Janeiro até São Paulo\n'+
                           'SR - De São Paulo até Rio de Janeiro\n'+
                           'BS - De Brasília até São Paulo\n'+
                           'SB - De São Paulo até Brasília\n'+
                           'BR - De Brasília até Rio de Janeiro\n'+
                           'RB - Rio de Janeiro até Brasília\n'+
                           '>> ') #Entrada de Menu para o usuário indicar a rota
        if rotaObjeto == 'RS': #Declarando a rota e o retorno
            return 1
        elif rotaObjeto == 'SR':
            return 1
        elif rotaObjeto == 'BS':
            return 1.2
        elif rotaObjeto == 'SB':
            return 1.2
        elif rotaObjeto == 'BR':
            return 1.5
        elif rotaObjeto == 'RB':
            return 1.5
        else: #Caso a rota não esteja entre as opções do menu, será exibido no console as seguintes frases
            print('Você digitou uma rota que não existe.')
            print('Por favor, entre com a rota desejada novamente.')
            continue #E volta para o inicio do laço para que digite opção válida
#Término da função rotaObjeto()

#Inicio do programa
print('Bem Vindo a Companhia de Logistica da Mayara Castro S.A.') #Identificador pessoal
#Organizando a ordem das "def" e declarando as variáveis para o print (cálculo final).
dimensoes = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
print('Total a pagar(R$): R${:.2f}. (Dimensões: {:.2f} * Peso: {:.2f} * Rota: {:.2f})'.format(dimensoes * peso * rota, dimensoes, peso, rota))
