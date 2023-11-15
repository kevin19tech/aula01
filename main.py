import time

import numpy

# array: aceitam dados apenas do mesmo tipo - ganha desempenho

# 1 - exemplo 1
#vetor
#ndarray1 = numpy.zeros(100000)
#print(f' 1- Conteúdo da Lista: {ndarray1}, o tamanho: {len(ndarray1)}')
#ndarray1 = numpy.ones(100000)
#print(f' 2- Conteúdo da Lista: {ndarray1}, o tamanho: {len(ndarray1)}')
# onde começa, qual número termina,
#ndarray1 = numpy.linspace(10,100,1000)
#print(f' 3- Conteúdo da Lista: {ndarray1}, o tamanho: {len(ndarray1)}')

# 2 - exemplo 2 - Comparar desempenho
# modulo time
# tem que importar
#start_time = time.time()
#lista = [0] * 1000000000
#end_time = time.time()
#elapsed_time = end_time - start_time
# print(f'A criação de lista de 1 bilhão de elementos levou: {elapsed_time}')

#start_time = time.time()
#ndarray = numpy.zeros(1000000000)
#end_time = time.time()
#elapsed_time = end_time - start_time
#print(f'A criação de lista de 1 bilhão de elementos levou: {elapsed_time}')

# 3- deifinindo tipo ganha desempenho
start_time = time.time()
#normal é 64 bit - então pode definir bit menor pra ganhar desempenho
ndarray_uint8 = numpy.zeros(1000000000, dtype='uint8')
end_time = time.time()
elapsed_time = end_time - start_time
print(f'A criação de lista de 1 bilhão de elementos levou: {elapsed_time}')

#Matrizes

rng = numpy.random.default_rng()
vetor=rng.random(4)
print(vetor)

#4- ordenar vetores
#sort
#m_coluna = numpy.sort()


# 5 - graficos


import plotly.express

array_a = numpy.loadtxt('vetor_a.txt',dtype=numpy.float64, delimiter=';')
array_b = numpy.loadtxt('vetor_b.txt',dtype=numpy.float64, delimiter=';')
array_c = numpy.loadtxt('vetor_c.txt',dtype=numpy.float64, delimiter=';')
print(array_a)

array_abc = numpy.vstack([array_a,array_b,array_c])
print(array_abc)
array_abc = array_abc.transpose()
print(array_abc)
fig = plotly.express.line(array_abc)
fig.show()