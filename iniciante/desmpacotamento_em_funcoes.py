"""
Desempacotamento em chamadas de metodos e funcções
"""

string = 'ABCD'
lista = ['Charles', 'David', 1, 2, 3, 'Verlim']
tupla = 'Python', 'é', 'legal'
salas = [
    #   0          1
    ['Charles', 'David'], # 0
    #   0
    ['Verlim'], # 1
    #   0    
    ['Zacharczuk'],#, (0, 10, 20, 30, 40)], # 2
]

# p, b, *_, ap, u = lista
# print(p, u)

# for nome in lista:
#     print(nome, end=' ')

print(*lista)
print(*string)
print(*tupla)
print(*salas, sep='\n')