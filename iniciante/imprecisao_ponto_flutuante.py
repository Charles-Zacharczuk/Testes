"""
Imprecisão de ponto futuante
Double precision floating point format IEEE 754
"""
numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}') #str
print(round(numero_3, 1)) #float