import matplotlib.pyplot as plt

def generate_charts():
    labels = ['a', 'b', 'c']
    values = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()