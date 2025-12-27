frase = (
    "O Python é uma linguagem de programação"
    "multiparadigma."
    "Python foi criado por Guido van Rossum."
)

i = 0
qtd_ap_mais_vz = 0
letra_ap_mais_vz = ""

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == " ":
        i += 1
        continue

    qtd_ap_mais_vz_atual = frase.count(letra_atual)

    if qtd_ap_mais_vz < qtd_ap_mais_vz_atual:
        qtd_ap_mais_vz = qtd_ap_mais_vz_atual
        letra_ap_mais_vz = letra_atual

    i += 1

print(
    "A letra que apareceu mais vezes foi "
    f'"{letra_ap_mais_vz}" que apareceu '
    f"{qtd_ap_mais_vz}x"
)
