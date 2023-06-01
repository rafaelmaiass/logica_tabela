################## Importar a tabela ##################
from prettytable import PrettyTable
################## Boas Vindas ##################
print('Bem vindo a Lanchonete do Cruzeirão Cabuloso\n')
################## o Cardápio visual ##################
print('+=============== Cardápio ===================+')
cardapio = PrettyTable()
cardapio.field_names = ['Código', 'Descrição', 'Valor(R$)']
dados = [
    [100, 'Cachorro-Quente', 9.00],
    [101, 'Cachorro-Quente Duplo', 11.00],
    [102, 'X-Egg', 12.00],
    [103, 'X-Salada', 13.00],
    [104, 'X-Bacon', 14.00],
    [105, 'X-Tudo', 17.00],
    [200, 'Refigerante Lata', 5.00],
    [201, 'Chá Gelado', 4.00]
]
for linha in dados:
    cardapio.add_row(linha)
print(cardapio)
################## Cardápio interno ##################
lista_dados = []
for linha in cardapio._rows:
    lista_dados.append(list(linha))
################## Salvar Pedidos ##################
pedidos = 0
################## Toda a lógica ##################
while True:
    print()

    pedido = int(input('Faça um pedido.\nDigite o codigo do alimento desejado: '))
    codigo = False
    
    for codigos in lista_dados:
        if pedido in codigos:
            codigo = True
            break

    if codigo:
        print()
        print(f'Voce pediu um {codigos[1]} no valor de R${codigos[2]}')
        pedir_dnv = input(f'Gostaria de pedir mais alguma coisa? (s)sim/(n)não: \n')
        pedidos += codigos[2]
        if pedir_dnv == 's':
            continue

        elif pedir_dnv == 'n':
            print()
            print(f'O total a ser pago é: R${pedidos}')
            print('Obrigado e que o Cruzeiro amasse o Gremio hoje.')
            break

        else:
            print('Voce não digitou (s) ou (n)\nDigite novamente se deseja pedir novamente ou não.')  

    else:
        print('Pedido inválido.\nDigite um número do cardápio.')
        continue
    ################## Fim ##################    
    
