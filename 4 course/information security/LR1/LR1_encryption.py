# алфавит
# cyrillic = [chr(i) for i in range(ord('а'), ord('я') + 1)]
# cyrillic_str = ''.join(cyrillic)
cyrillic_str = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
key = open('key.txt', 'r', encoding='utf-8').read()
message = open('message.txt', 'r', encoding='utf-8').read()

def get_matrix(key, cyrillic_str):
    matrix = [["0","0","0","0","0","0"],
              ["0","0","0","0","0","0"],
              ["0", "0", "0", "0", "0", "0"],
              ["0","0","0","0","0","0"],
              ["0","0","0","0","0","0"],
              ["0","0","0","0","0","0"],]
    dictionary = (" ".join(dict.fromkeys(key + cyrillic_str))).replace(" ","")+"123"
    print("Алфавит: ",dictionary)
    k = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = dictionary[k]
            k+=1
            #print(matrix[i][j], end=" ")
        #print()
    return matrix

def show_matrix(matrix):

    print("Полученная матрица:")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()

def get_bigramm(message):
    bi = []
    i = 0
    print("Исходное сообщение: ", message)
    mess = message.replace(" ","")
    while i < (len(mess)-1):

        buff = mess[i]+mess[i+1]
        if(mess[i]==mess[i+1]):
            buff = mess[i]+"я"
            i += 1
        else: i+=2
        bi.append(buff)

        if i == len(mess)-1:
            buff = mess[i] + "я"
            bi.append(buff)
    print("Биграмма: ", bi)
    return bi


def encryption():
    str = ''
    def search_coor(n1, n2):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (matrix[i][j]==n1):
                    x1,y1 = i,j
                if (matrix[i][j]==n2):
                    x2,y2 = i,j
        coor = {'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2}
        return coor

    matrix = get_matrix(key, cyrillic_str)
    bi = get_bigramm(message)
    show_matrix(matrix)

    for i in range(len(bi)):
        b1, b2 = bi[i][0], bi[i][1]
        cr = search_coor(b1, b2)
        #если на одной строке
        if(cr['x1']==cr['x2']):
            if(cr['y1']==5):
                b1 = matrix[cr['x1']][0]
            else:
                b1 = matrix[cr['x1']][cr['y1']+1]
            if(cr['y2'] == 5):
                b2 = matrix[cr['x2']][0]
            else:
                b2 = matrix[cr['x2']][cr['y2']+1]
            str += b1 + b2

        #если в одном столбце
        elif(cr['y1']==cr['y2']):
            if(cr['y1']==5):
                b1 = matrix[0][cr['y1']]
            else:
                b1 = matrix[cr['x1']+1][cr['y1']]
            if (cr['y2'] == 5):
                b2 = matrix[0][cr['y2']]
            else:
                b2 = matrix[cr['x2'] + 1][cr['y2']]

            str += b1 + b2

        #если в разных
        else:
            b1 = matrix[cr['x1']][cr['y2']]
            b2= matrix[cr['x2']][cr['y1']]
            str += b1 + b2
    #print(str)
    return str


#сюда особо не смотри, он немного криво сделан, в частности буква "я" там неправильно реализована
# я просто по лайту написал, чтобы себя проверить
def bigram_dec(message):
    bi = []
    i=0
    print("Принятое сообщение: , ", message)
    while i < (len(message)-1):
        buff = message[i]+message[i+1]
        bi.append(buff)
        i+=2
    return bi


def decoding(mess):
    str = ''

    def search_coor(n1, n2):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (matrix[i][j] == n1):
                    x1, y1 = i, j
                if (matrix[i][j] == n2):

                   x2, y2 = i, j
        coor = {'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2}
        return coor

    matrix = get_matrix(key, cyrillic_str)
    bi = bigram_dec(mess)

    for i in range(len(bi)):
        b1, b2 = bi[i][0], bi[i][1]
        cr = search_coor(b1, b2)
        # если на одной строке
        if (cr['x1'] == cr['x2']):
            if (cr['y1'] == 0):
                b1 = matrix[cr['x1']][5]
            else:
                b1 = matrix[cr['x1']][cr['y1'] - 1]
            if (cr['y2'] == 0):
                b2 = matrix[cr['x2']][5]
            else:
                b2 = matrix[cr['x2']][cr['y2'] - 1]
            str += b1 + b2

        # если в одном столбце
        elif (cr['y1'] == cr['y2']):
            if (cr['y1'] == 0):
                b1 = matrix[5][cr['y1']]
            else:
                b1 = matrix[cr['x1'] - 1][cr['y1']]
            if (cr['y2'] == 0):
                b2 = matrix[5][cr['y2']]
            else:
                b2 = matrix[cr['x2'] - 1][cr['y2']]

            str += b1 + b2
        #       print('2: ',b1,b2)

        # если в разных
        else:
            b1 = matrix[cr['x1']][cr['y2']]
            b2 = matrix[cr['x2']][cr['y1']]
            str += b1 + b2

    print('Расшифрованное сообщение: ', str)

ms = encryption()

print('Зашифрованное сообщение: ',ms)
decoding(ms)