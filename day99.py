# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

n,m,p=map(int, input().split())
matrix_a = numpy.array([input().split() for _ in range(n)], int)

matrix_b = numpy.array([input().split() for _ in range(m)], int)

print(numpy.concatenate((matrix_a, matrix_b), axis=0))