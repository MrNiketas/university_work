import math

def set_parametr():
    a = 0
    b = 4
    E = 0.01
    return a, b, E
def func(x):
    return x ** 3 - 3 * x + 2
def start():
    a, b, E = set_parametr()
    counter = 0
    max_counter = 200

    while abs(b - a) >= E:

        counter += 1
        print('Шаг №{counter}'.format(counter=counter))
        x1 = a + 0.25*(b-a)
        x2 = b - 0.25*(b-a)
        if func(x1) < func(x2):
            b = x2
            print('x= ',b)
            print('f(x)= ',func(x2))
        if func(x1) > func(x2):
            a = x1
            print('x= ',a)
            print('f(x)= ',func(x1))
        if func(x1) == func(x2):
            b = x2
            print('x= ',b)
            print('f(x)= ',func(x2))

print('Метод половинного деления:')
start()
