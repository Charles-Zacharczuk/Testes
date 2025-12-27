"""
Introdução ao desempacotamento + tubles (tuplas)
"""

# nomes = ['Charles', 'David', 'Zacharczuk']
# nome1, nome2, nome3 = ['Charles', 'David', 'Zacharczuk']
# nome1,*_ = ['Charles', 'David', 'Zacharczuk']
# _, nome,*_=['Charles', 'David', 'Zacharczuk']
# _, _, nome,*_=['Charles', 'David', 'Zacharczuk']

# print(nome)

"""
Tubles (tuplas) - Uma lista imutavel
"""
# nomes = 'Charles', 'David', 'Zacharczuk' 
nomes = ['Charles', 'David', 'Zacharczuk'] 
nomes = tuple(nomes)
nomes = list(nomes)
print(nomes[1])
