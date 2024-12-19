def sum(a, b):
    """
    >>> sum(5, 7)
    12

    >>> sum(4, -4)
    0
    """
    return a + b


def sustract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):

    '''
    >>> division(10, 0)
    Traceback (most recent call last):
    ValueError: La division por 0 no esta permitida
    '''
    if b == 0:
        raise ValueError('La division por 0 no esta permitida')
    return a / b