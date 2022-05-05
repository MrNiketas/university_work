e = 0.01
a = 0
b = 4

def func(x):
    return x ** 3 - 3 * x + 2

counter = 0
max_counter = 200
fib1 = 1
fib2 = 1
while (b - a) > e:
    n = (b - a)/e
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1

    counter += 1
    print('Шаг №{counter}'.format(counter=counter))
    x1 = b - (fib1 / fib2) * (b - a)
    x2 = a + (fib1 / fib2) * (b - a)
    if func(x1) < func(x2):
        a = a
        b = x2
    else:
        a = x1
        b = b

m = (b + a) / 2
print('x= ', m)