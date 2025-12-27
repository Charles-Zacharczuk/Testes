"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai pegar uma palavra secreta qualquer e vai dar a possibilidade
para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada
está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta: Exiba a letra
    - Se a letra digitada não estiver na palavra secreta: exiba *.
Faça contagem de tentativas do usuário
"""

# palavra = "Ially".upper()
# palavra_digitada = ''
# repeticoes = 0

# while palavra != palavra_digitada:
#     palavra_digitada = input(f"Digite uma letra ({repeticoes}x: )").upper()

#     repeticoes += 1

#     if repeticoes == 10:
#         print(f"Você perdeu, a palavra era {palavra}")
#         break
#     else:
#         continue

import os

palavra_secreta = "amor"
letras_acertadas = ""
numero_tentativas = 0

print(
    'Descubra a palavra, você tem 10 tentivas, digite apenas " 1 " letra por vez\
 cada " * " representa uma letra, e será mostrado somente após a primeira tentativa'
)
while True:

    letra_digitada = input("Digite uma letra: ")
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print("Digite apenas uma letra.")
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"

    print(f"Palavra formada: {palavra_formada}")

    if palavra_formada == palavra_secreta:
        os.system("clear")
        print("Você ganhou!")
        print(f"A palavra era {palavra_secreta}")
        letras_acertadas = ""
        numero_tentativas = 0
