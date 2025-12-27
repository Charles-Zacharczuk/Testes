"""
CPF = 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma 
contagem regressiva começando do 10

Ex.: 746.824.890-70 (746824890)
  10 9  8  7  6  5  4  3  2
* 7  4  6  8  2  4  8  9  0
  70 36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 / 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0 
Caso contráriodiso:
    resultado é o valor da conta

O primeiro digito do CPF é 7
"""
"""
Cácule o segundo digito do CPF
CPF = 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF,
Mais o primeiro digito,
multiplicando cada um dos valo por uma
contagem regressiva começando de 11

Ex.: 746.824.890-70 (746824890)
  11 10 9  8  7  6  5  4  3  2
* 7  4  6  8  2  4  8  9  0  7 < -- Primeiro digito
  77 40 54 64 14 24 40 36 0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo digito do CPF é 0
"""
# cpf = '36440847007' # Esse CPF gera o primeiro digito como 10 (0)
import re
import sys

entrada = input('CPF: ')

cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
)

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    sys.exit

nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10
contador_regressivo_2 = 11

resultado_1 = 0
resultado_2 = 0
for digito in nove_digitos:
    resultado_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado_1 * 10) % 11

digito_1 = 0 if digito_1 >=9 else digito_1

# print(digito_1)

dez_digitos = nove_digitos + str(digito_1)

for digito_2 in dez_digitos:
    resultado_2 += (int(digito_2)) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_2 * 10) % 11
digito_2 = 0 if digito_2 >= 9 else digito_2

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF inválido')