import socket
import math
import json
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
STR_Alphabet = "11абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def Euclid(a, b): # функция Евклида
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return max(a, b)

def EulerFunction_Euclid(n): # функция Эйлера через Евклида
    result = []
    for i in range (1,n):
        if Euclid(n,i) == 1:
            result.append(i)
    return result

def gcdExtended(a, b):
    if a == 0 :
        return b,0,1
    gcd,x1,y1 = gcdExtended(b%a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcd,x,y

def method(data):

    print("Первый порядок: ")
    key = data.get("firstKey")
    message = data.get("firstMessage")
    message = methodPoryadok(key,message,1)
    strArray = list(STR_Alphabet)
    T = []
    for i in message:
        T.append(strArray[i])
    message = T
    print(T)

    print("Второй порядок: ")
    key = data.get("secondKey")
    message = data.get("secondMessage")
    message = methodPoryadok(key,message,2)
    strArray = list(STR_Alphabet)
    T = []
    for i in message:
        T.append(strArray[i])
    message = T
    print(T)

    print("Третий порядок: ")
    key = data.get("thirdKey")
    message = data.get("thirdMessage")
    message = methodPoryadok(key,message,3)
    strArray = list(STR_Alphabet)
    T = []
    for i in message:
        T.append(strArray[i])
    message = T
    print(T)

    print("Четвертый порядок: ")
    key = data.get("quadKey")
    message = data.get("quadMessage")
    message = methodPoryadok(key,message,4)
    strArray = list(STR_Alphabet)
    T = []
    for i in message:
        T.append(strArray[i])
    message = T
    print(T)
    return 0

def methodPoryadok(key,message,order):
    if(order == 1):
        n = int(key[0])
        e = int(key[1])
        ne = n-1
    elif(order == 2):
        n = int(key[0])
        e = int(key[1])
        ne = (int(key[2][0])-1)*(int(key[2][1])-1)
    elif(order == 3):
        n = int(key[0])
        e = int(key[1])
        ne = int(int(key[2][0])**int(key[2][1]) - int(key[2][0])**(int(key[2][1])-1))
    elif(order == 4):
        p = key[2]
        q = key[3]
        n = int(key[0])
        e = int(key[1])
        for k in range(0,len(p),1):
            n *= int(p[k])**int(q[k])
        ne = n
        for k in range(0,len(p),1):
            ne *= (1-1/int(p[k])) 
        ne = int(ne)
    
    keyCode = []
    x,y,d = gcdExtended(ne,e)
    keyCode.append(n)
    keyCode.append(d)
    print("D:",d,"E:",e,"N:",n,"NU:",ne)
    print("Check D:", d*e,"mod",ne,"=",(d*e)%ne)
    print()
    print("Key:",keyCode)
    messageCode = parseMessage(keyCode,message)
    print(messageCode)
    print()
    return messageCode

# Принимает (key(list) , message(list)) 
# key - ключ [ n , e ] ; message - сообщение [];
# Возвращает message(list)
def parseMessage(key,message): 
    C = []
    for i in range(0,len(message),1):
        C.append(message[i]**int(key[1]) % int(key[0]))
    return C

def startServer():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024)
            data = json.loads(data.decode())
            method(data)
                
if __name__ == '__main__':
    startServer()