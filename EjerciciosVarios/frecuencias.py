import random

# Poblacion
datos = list(range(100))
for i in range(0,100):
    datos[i] = random.randrange(1,6,1)      #datos es mi poblacion

n = [1, 2, 3, 4, 5]

#-----------------------------------------------------------------------------------------
frecAbs = list(range(5))

for i in range(0,5):
    cont = 0
    for j in range(0, len(datos)):
        if n[i] == datos[j]:
            cont += 1
    frecAbs[i] = cont

print(frecAbs) #La suma de la lista que se presente debe dar 100

# --------------------------------------------------------------------------------------
# Frecuencia Relativa
fre = list(range(5))

for i in range(0,5):
    fre[i] = frecAbs[i]/100

print(fre)
print(sum(fre))