cyrillic_str = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
key = open('key.txt','r', encoding='utf-8').read()
message = open('message.txt', 'r', encoding='utf-8').read()
N = 33

def get_numbers(text):
    buff = []
    for i in range(len(text)):
        bf = 0
        for j in range(len(cyrillic_str)):
            if (text[i]==cyrillic_str[j]):
                bf = j
        buff.append(bf)
    return buff

def get_litters(res):
    str = ''
    for i in range(len(res)):
        str += cyrillic_str[res[i]]
    return str

def get_gamma(key, mess):
    if(len(key)<(len(mess))):
        while len(key)<(len(mess)):
            key += key
    key = key[:len(mess)]
    return get_numbers(key)

def encryption(message):
    C = []
    P = get_numbers(message)
    K = get_gamma(key, message)
    for i in range(len(P)):
        sum = (P[i]+K[i]) % N
        C.append(sum)
    return C
print('P:')
print(get_numbers(message))
print('K:')
print(get_gamma(key, message))
print('Числовая последовательность зашифрованного сообщения :')
print(encryption(message))
print('Зашифрованное сообщение: ', get_litters(encryption(message)))


