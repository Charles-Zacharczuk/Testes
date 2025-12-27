nome = "Charles"
altura = 1.76
peso = 95
imc = peso / (altura *altura)

# print(nome, "tem", altura, "de altura, pesa", peso, "quilos e seu IMC é:", imc)

linha_1 = f'{nome} tem {altura:.10f} de altura'
print(linha_1)
linha_2 = f"pesa {peso} quilos e seu imc é:"
print(linha_2)
linha_3 = f'{imc:.2f}'
print(linha_3)