"""
Lista de listas e seus indices
"""

salas = [
    #   0          1
    ['Charles', 'David'], # 0
    #   0
    ['Verlim'], # 1
    #   0    
    ['Zacharczuk'],#, (0, 10, 20, 30, 40)], # 2
]

# print(salas[2][1][2])
# salas[0][1] = 'charles'
# print(salas[0][1])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
