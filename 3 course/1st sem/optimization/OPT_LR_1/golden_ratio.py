def set_parametr():
    a = 0
    b = 4
    E = 0.01
    return a, b, E

def func(x):
    return x ** 3 - 3 * x + 2


a, b, E = set_parametr()
counter = 0
max_counter = 200
x1 = a+0.382*(b-a)
x2 = b-0.382*(b-a)
A = func(x1)
B = func(x2)

while b - a >= E:

    counter += 1
    print('Шаг №{counter}'.format(counter=counter))

    if(A<B):
        b = x2
        x2 = x1
        B = A
        x1 = a+0.382*(b-a)
        A = func(x1)
        print('a= ',a)
        print('b= ', b)

    if(A>B):
        a = x1
        x1 = x2
        A = B
        x2 = b-0.382*(b-a)
        B = func(x2)
        print('a= ', a)
        print('b= ', b)

x = (a+b)/2
print('Ответ:\n', 'x= ', x)