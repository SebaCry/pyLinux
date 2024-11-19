def sum(a, b):
    return a + b

def sustract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError('La division por 0 no esta permitida')
    return a / b