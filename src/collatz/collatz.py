import sys
import matplotlib.pyplot as plt

def iteraciones_collatz(n):
    iteraciones = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        iteraciones += 1
    return iteraciones

iteraciones_x = []
numeros_y = []

for n in range(1, 10001):
    iteraciones_x.append(iteraciones_collatz(n))
    numeros_y.append(n)

plt.scatter(iteraciones_x, numeros_y, s=1, color='violet')
plt.title('Conjetura de Collatz (1 a 10000)')
plt.xlabel('Número de iteraciones')
plt.ylabel('Número n de comienzo')
plt.show()