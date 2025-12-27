"""
For + Range
range -> range(start, stop, step)
"""

# numeros = range(1,     10,     2)

# for numero in numeros:
#     print(numero)

"""
Iterável -> str, range, etc (__iter__)
iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> nme entrega seu iterador
"""

# texto = iter("Charles")
# print(next(texto))
# print(texto.__next__)

texto = "Charles"
iterador = iter(texto)
numeros = 1
texto_1 = ""
while True:
    try:
        print(next(iterador))
    except StopIteration:
        break

for letra in texto:
    texto_1 += f"*{letra}"
    print(letra)
print(texto_1)
