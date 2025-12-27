"""
Introdução de funções (def) em Python
Funções são trechos de código usados para
realizar determinada ação ao longo do seu código.
ELas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções retornam None (nada)
"""

# def Print():
#     print('Oi')
#     print('Oi')
#     print('Oi')
#     print('Oi')
#     print('Oi')
#     print('Oi')
#     print('Oi')

# Print()

# def imprimir(a, b, c): <- Paremetro dentro dos paranteses
#     print(a, b, c)

# imprimir(1, 2, 3) <- argumento dentro dos parenteses
# imprimir(4, 5, 6)

# def saudacao(nome = 'Sem nome'):
#     print(f'Olá, {nome}!')

# saudacao("Charles")
# saudacao("David")
# saudacao("Verlim")
# saudacao("Zacharczuk")
# saudacao()


def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f"{numero} é multiplo de {multiplo}", end=" ")
    print(resultado)


multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)
