"""
Cuidados com dados mutáveis
= - copiado o valor (imutável)
= - aponta para o mesmo valor na memoria (mutável)
"""

# nome = 'Charles'
# outra_variavel = nome
# nome = 'David'

# print(outra_variavel)
# print(nome)

lista_a = [1, 2]
# lista_b = lista_a
lista_b = lista_a.copy()
lista_a[0] = 3

print(lista_b)
print(lista_a)
