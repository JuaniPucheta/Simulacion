import matplotlib.pyplot as plt
import random as ran
import numpy as np

nrosTiros = []
prom = []
desv = []
varianza = []
frecRelativa = []


def promedio(repeticiones):
    cont = 0
    sum = 0

    while cont <= repeticiones:
        sum += ran.randint(0, 36)
        cont += 1
        nrosTiros.append(cont)
        prom.append(sum / cont)

    return (sum / repeticiones)


def desvio(repeticiones, media):
    cont = 0
    sum = 0

    while cont <= repeticiones:
        sum += ran.randint(0, 36)
        cont += 1
        desv.append((cont - media) ** 2 * 1 / sum)

    return (np.std(desv))


repeticiones = int(input("Ingrese la cantidad de repeticiones: "))

media = promedio(repeticiones)
desvio(repeticiones, media)

# ---------------------------Graficas---------------------------------------------
fig, ax = plt.subplots(1, 2, sharex=True, sharey=True)

ax[0].plot(nrosTiros, prom, color='g', label='Promedio')
ax[0].legend()
ax[0].plot([10, 20, 30])

ax[1].plot(nrosTiros, desv, color='r', label='Desvio')
ax[1].legend()

'''
    fig1, ax1 = plt.subplots(1, 2, sharey=True)

    ax1[0].plot(nrosTiros, frecRelativa, color='g', label='Frecuencia relativa')
    ax1[0].legend()
    ax1[1].plot(nrosTiros, varianza, color='r', label='Varianza')
    ax1[1].legend()
'''

plt.show()
