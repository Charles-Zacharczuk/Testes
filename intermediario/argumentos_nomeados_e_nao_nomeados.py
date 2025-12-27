"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# def soma(x, y): # Definição de função
#     print(x + y)

def soma(x, y):  # Parametro
    print(f"{x=} {y=}", "|", "x +y  = ", x + y)

soma # nome da função
soma() # execução da função
soma(5, 10)  # argumento posicional
soma(y=1, x=10)  # argumento nomeado
