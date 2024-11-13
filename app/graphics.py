'''import matplotlib.pyplot as plt

# Crear datos de prueba
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Crear un gráfico simple
plt.plot(x, y)
plt.title("Test Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()'''

import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
    
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig('bar.png')
    plt.close()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig('chart_pie_finalfinal.png')
    plt.close()

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [143, 254, 1029]
    ##generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)

'''import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([1,3,5,23,14])

plt.plot(ypoints)
plt.show()'''
