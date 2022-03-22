import matplotlib.pyplot as plt

# pais 1
x = [2016, 2017, 2018, 2019, 2020]
y = [10, 13, 17, 18, 19]

#pais 2
x2 = [2016, 2017, 2018, 2019, 2020]
y2 = [19, 13, 25, 27, 30]

x3 = [2016, 2017, 2018, 2019, 2020]
y3 = [19, 13, 25, 27, 30]

x4 = [2016, 2017, 2018, 2019, 2020]
y4 = [19, 13, 25, 27, 30]


fig, ax = plt.subplots(1, 2, sharey=True)

ax[0].plot(x,y, color='g', label='Colombia')
ax[0].legend()
ax[1].plot(x2, y2, color='r', label='Argentina')
ax[1].legend()

fig1, ax1 = plt.subplots(1, 2, sharey=True)

ax1[0].plot(x3,y3, color='g', label='asd')
ax1[0].legend()
ax1[1].plot(x4, y4, color='r', label='zxc')
ax1[1].legend()

plt.show()