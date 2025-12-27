"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no indice escolhido
    pop    - Remove no final ou do indice escolhido
    del    - Apaga um indice
    clear  - Limpa a lista
    extend - Estende a lista
    +      - Concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#         01234
#        -54321
# string = 'ABCDE' # 5 caracteres
# print(bool([])) #falsy
# print(lista, type(lista))

# indices:   0    1        2       3    4
#          -5   -4       -3      -2   -1
# lista = [123, True, 'Charles', 1.2, []]
# print(lista)
# print(lista[2], type(lista[2]))
# lista[-3] = 'David'
# print(lista[2])

# lista = [10, 20, 30, 40]
# numero = lista[2]
# lista[2] = 300
# del lista[3]
# print(lista)
# print(lista[2])
# lista.append(50)
# lista.pop(1)
# lista.append(60)
# lista.append(70)
# lista.pop()
# print(lista)

# lista = [10, 20, 30, 40]
#          indice   valor
# lista.insert(0, 'Charles')
# print(lista)
# lista.clear()
# print(lista)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)
print(lista_c)
