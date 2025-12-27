# entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'impar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')


# hora_atual = input('Digite o horário: ')

# if hora_atual >= 0 and hora_atual<= 11 :
#     print('Bom dia')
# if hora_atual >= 12 and hora_atual<= 17 :
#     print('Boa tarde')
# if hora_atual >= 18 and hora_atual<= 23 :
#     print('Boa noite')

# try:
#     hora = int(hora_atual)

#     if hora >= 0 and hora <= 11:
#         print('Bom dia')
#     elif hora >= 12 and hora <= 17:
#         print('Boa tarde')
#     elif hora >= 18 and hora <= 23:
#         print('Boa noite')
#     else:
#         print('Não conheço essa hora')
# except:
#     print('Por favor, digite apenas números inteiros')


primeiro_nome = input("Digite o seu primeiro nome: ")
tamanho_nome = len(primeiro_nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print("Seu nome é curto")
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")
else:
    print("Digite mais de uma letra")
