import socket as socket
HOST = "172.19.98.129"  # The server's hostname or IP address
PORT = 8989  # The port used by the server
LEN_ARRAY=6
STR_Alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def parsePackage(key,message):
    keyCoder = createKeyCoder(key)
    message = createMessageBigramm(message)
    messageCoder = startMethodPlayfair(keyCoder,message)
    return messageCoder

def createKeyCoder(key):
    key = key.lower() # Преобразование ключа в нижний регистр

    keyCoder = [] # Инициализация массива
    for i in range(0,LEN_ARRAY,1):
        keyCoder.append([""]*LEN_ARRAY)
    
    dictionary = (" ".join(dict.fromkeys(key + STR_Alphabet))).replace(" ","")+"123" #Заполнение массива ключа
    for i in range(0,LEN_ARRAY,1):
        for j in range(0,LEN_ARRAY,1):
            keyCoder[i][j]=dictionary[i*LEN_ARRAY+j]
    
    print("Ключ шифрования: ")
    for i in keyCoder:
        print(i)
    print()

    return keyCoder

def createMessageBigramm(message):
    helpBuffer = []
    message = message.replace(" ","")
    message = message.lower()
    message = list(message)
    if ((len(message) % 2) == 1):
        message.append("я")
    for i in range(0,len(message),2):
        helpBuffer.append(message[i]+message[i+1])
    
    for i in helpBuffer:
        if(i[0] == i[1]):
            i[1] = "я"
        if(i[0] == i[1]):
            i[1] = "х"
    
    print("Биграмма сообщения:")
    print(helpBuffer)
    print()

    return helpBuffer

def startMethodPlayfair(keyCoder,message):
    coderMessage = []
    for msg_line in message:
        msg_char = list(msg_line)
        x1,x2,y1,y2 = 0, 0, 0 , 0
        for i in range(0,LEN_ARRAY,1):
            for j in range(0,LEN_ARRAY,1):
                if msg_char[0] == keyCoder[i][j]:
                    x1,y1 = i, j
                if msg_char[1] == keyCoder[i][j]:
                    x2,y2 = i, j
        if x1 == x2:
            if y1 == LEN_ARRAY-1:
                msg_char[0] = keyCoder[x1][0]
                msg_char[1] = keyCoder[x2][y2+1]
            elif y2 == LEN_ARRAY-1:
                msg_char[0] = keyCoder[x1][y1+1]
                msg_char[1] = keyCoder[x2][0]
            else:
                msg_char[0] = keyCoder[x1][y1+1]
                msg_char[1] = keyCoder[x2][y2+1]
        elif y1 == y2:
            if x1 == LEN_ARRAY-1:
                msg_char[0] = keyCoder[0][y1]
                msg_char[1] = keyCoder[x2+1][y2]
            elif x2 == LEN_ARRAY-1:
                msg_char[0] = keyCoder[x1+1][y1]
                msg_char[1] = keyCoder[0][y2]
            else:
                msg_char[0] = keyCoder[x1+1][y1]
                msg_char[1] = keyCoder[x2+1][y2]
        else:
            msg_char[0] = keyCoder[x1][y2]
            msg_char[1] = keyCoder[x2][y1]
        coderMessage += msg_char
    
    coderMessage = "".join(coderMessage)
    print("Закодированное сообщение")
    print(coderMessage)
    print
    return coderMessage

def startClient(key, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = parsePackage(key, message)
        data = key + " " + data
        s.sendall(data.encode())

if __name__ == '__main__':
    print("Введите ключ шифрования: ")
    key = str(input())
    print()

    print("Введите сообщение:")
    message = str(input())
    print()

    startClient(key, message)
