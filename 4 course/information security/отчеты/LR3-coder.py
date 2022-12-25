import socket as socket
import math
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
STR_Alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
N = 33

def method(key, message):
    strArray = list(STR_Alphabet)
    C = []
    P = []
    K = []
    for i in range(0,len(key),1):
        for j in range(0,len(STR_Alphabet)-1,1):
            if key[i]==STR_Alphabet[j]:
                K.append(j)
    k=1
    while len(K)<len(message):
        K.append(K[k-1])
        k+=1         
    for i in range(0,len(message),1):
        for j in range(0,N,1):
            if message[i]==strArray[j]:
                P.append(j)
        C.append((P[i]+K[i]) % N)

    print("P:",P)
    print("K:",K)
    print("C:",C)
    
    msg = []
    for i in range(0,len(message),1):
        msg.append(strArray[C[i]])
    msg="".join(msg)
    print(msg)
    return msg

def startClient(key, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = method(key, message)
        data =  key + " " + data
        s.sendall(data.encode())


if __name__ == '__main__':
    print("Введите значение гамма-ключа : ")
    key = str(input())
    print()
    print("Введите сообщение:")
    message = str(input())
    message = message.replace(" ","")
    print()
    startClient(key, message)
   