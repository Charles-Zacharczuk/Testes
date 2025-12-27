"""
Faça uma lista de compras com list
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de incides inexistentes na lista
"""

import os

lista = []

while True:
    print('Lista de compras')
    print('1 - Inserir')
    print('2 - Apagar')
    print('3 - Listar')
    opcao = input('Selecione uma opção: ')

    if opcao == '1':
        os.system('clear')
        produto = input('Produto: ')
        lista.append(produto)

    elif opcao == '2':
        os.system('clear')
        indice_str = input('Indice: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Digite um número inteiro')
        except IndexError:
            print('Indice não existe')   
                 
    elif opcao == '3':
        os.system('clear')
       
        if len(lista) == 0:
            print('Sua lista está vazia')

        for i, produto in enumerate(lista):
            print( i, produto)

       
    else:
        print('Escolha um opçao apresentada.')