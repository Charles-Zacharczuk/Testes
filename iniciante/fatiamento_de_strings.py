"""
Fatiamento de strings

 012345678
 Olá mundo
-987654321

Fatiamento [i:f:p ] [::]
i - inincio
f - fim
p - passo (quantidade que será contada por vez, 1 em 1, 2 pula 1 caracter....)
Obs.: a função len retorna a quantidade de caracters da str
"""
variavel = 'Olá mundo'
#print(variavel[5])
# print(variavel[-4])
# print(variavel[4:])
# print(variavel[4:8])
# print(variavel[0:5])
# print(variavel[-8:-2])
# print(variavel[3])
print(len(variavel[3]))
print(len(variavel))
print(variavel[0:len(variavel):1])
print(variavel[0:9:2])
print(variavel[::-1])
print(variavel[-1:-10:-1])