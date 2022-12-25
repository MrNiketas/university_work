from random import randint
p = 37
g = 2
x = 5
mess = [19, 6, 8, 1, 20, 17, 20, 18]
def get_key(p, g, x):
    y = g**x % p
    return y

def coder(p, g, x, y, mess):
    b = []
    T = mess
    for i in range (len(mess)-1):

        k = randint(1,p-1)
        a = g**k % p
        b[i] = (y**k * T[i]) % p
        return b
y = get_key(p, g, x)
print(coder(p, g, x, y, mess))

