"""
Enumerate - enumera iteraveis (indices)
"""

lista = ["Charles", "David", "Zacharczuk"]
lista.append("Verlim")

# lista_enumerada = enumerate(lista)


# for item in lista_enumerada):
# print(item)


# for item in enumerate(lista):
# print(item)


# lista_enumerada = list(enumerate(lista))

# print(lista_enumerada)

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)
