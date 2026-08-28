import numpy
print('criando uma matriz a partir de uma lista:')
l=[[3,4,5],[6,7,8],[9,0,1]]
Z=numpy.matrix(l)
print(Z)
print('trasposta da matriz:')
print(Z.T)
print('Invertsa da matriz:')
print(Z.I)
#criando outra matriz
R= numpy.matrix([[3,2,1]])
print('multiplicando matrizes:')
print(R * Z)
print('resolvendo um sistema linear:')
print(numpy.linalg.solve(Z,numpy.array([0,1,2]))) 
