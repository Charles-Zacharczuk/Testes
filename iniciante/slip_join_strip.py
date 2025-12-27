"""
split e join com list e str
split - divide uma string (retorna uma lista)
join - une uma string
strip - corta os espaços no final e no começo da str
"""
frase = "Olha só que, coisa interessante"
# lista_palavras = frase.split()
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases)
# print(lista_frases_cruas)
# frases_unidas = "*".join('ABC')
# print(f'*{frases_unidas}*')

frases_unidas = ', '.join(lista_frases)
print(frases_unidas)