import matplotlib.pyplot as plt

edades = [15, 16, 17, 20, 21, 21, 22, 23, 24, 25, 26, 30, 31, 32, 35]
bins = [15, 20, 25, 30, 35]

plt.boxplot(edades)
plt.show()
