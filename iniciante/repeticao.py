"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""

# condicao = 'True'

# while condicao:
#     nome = input('Digite o seu nome: ')
#     print(f'Seu nome é {nome}')

#     break

# contador = -1

# while contador <= 10:
#     contador = contador + 1
#     print(contador)


"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""

contador = -1

while contador <= 100:
    contador += 1

    if contador == 6:
        print(f"O {contador} não vai ser mostrado")
        continue

    if contador >= 10 and contador <= 27:
        print(f"O {contador} não vai ser mostrado")
        continue

    print(contador)

    if contador == 40:
        break
