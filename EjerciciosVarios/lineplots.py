import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))

# pais 1
x = [2016, 2017, 2018, 2019, 2020]
y = [10, 13, 17, 18, 19]

#pais 2
x2 = [2016, 2017, 2018, 2019, 2020]
y2 = [19, 13, 25, 27, 30]

plt.plot(x,y, marker = 'o', linestyle = '--', color = 'r', label='Argentina')
plt.plot(x2, y2, marker = 'd', linestyle = '-', color = 'g', label='Colombia')
plt.xlabel('Años')
plt.ylabel('Poblacion (M)')
plt.title('Años vs Poblacion')
plt.legend(loc='lower right')

plt.yticks([10, 40, 44])

plt.savefig('ejemplo.png')
plt.show()