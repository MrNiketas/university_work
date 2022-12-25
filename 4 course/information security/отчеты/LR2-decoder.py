import socket as socket
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

def parsePackage(massage,key):
    key = key.split(" ")
    helpBuffer = [[key[0],key[1]],[key[2],key[3]],[key[4],key[5]]]
    
    print(helpBuffer)
    return startMethod(helpBuffer,massage)

def startMethod(key,message):
    a = int(key[2][0])
    b = int(key[2][1])
    keyCoder = [] # Инициализация массива
    for i in range(0,a,1):
        keyCoder.append([""]*b)
    
    if (key[1][0]=='1'):
        if (key[1][1]=='3'):
            for i in range(0,a,1):
                for j in range(0,b,1):
                    keyCoder[i][j] = message[i*a+j] 
        if (key[1][1]=='4'):
            k=0
            for i in range(a-1,-1,-1):
                for j in range(0,b,1):
                    keyCoder[i][j] = message[k]
                    k+=1  
    if (key[1][0]=='2'):
        if (key[1][1]=='3'):
            k=0
            for i in range(0,a,1):
                for j in range(b-1,-1,-1):
                    keyCoder[i][j] = message[k]
                    k+=1
        if (key[1][1]=='4'):
            k=0
            for i in range(a-1,-1,-1):
                for j in range(b-1,-1,-1):
                    keyCoder[i][j] = message[k]
                    k+=1  
    if (key[1][0]=='3'):
        if (key[1][1]=='1'):
            k=0
            for i in range(0,b,1):
                for j in range(0,a,1):
                    keyCoder[j][i] = message[k]
                    k+=1
        if (key[1][1]=='2'):
            k=0
            for i in range(b-1,-1,-1):
                for j in range(0,a,1):
                    keyCoder[j][i] = message[k]
                    k+=1  
    if (key[1][0]=='4'):
        if (key[1][1]=='1'):
            k=0
            for i in range(0,b,1):
                for j in range(a-1,-1,-1):
                    keyCoder[j][i] = message[k]
                    k+=1
        if (key[1][1]=='2'):
            k=0
            print("4 2")
            for i in range(b-1,-1,-1):
                for j in range(a-1,-1,-1):
                    keyCoder[j][i] = message[k]
                    k+=1
    
    print()
    for i in keyCoder:
        print(i)
    print()
    massageCoder = []
    
    if (key[0][0]=='1'):
        if (key[0][1]=='3'):
            for i in range(0,a,1):
                for j in range(0,b,1):
                    massageCoder += keyCoder[i][j]
        if (key[0][1]=='4'):
            k=0
            for i in range(a-1,-1,-1):
                for j in range(0,b,1):
                    massageCoder += keyCoder[i][j]
    if (key[0][0]=='2'):
        if (key[0][1]=='3'):
            for i in range(0,a,1):
                for j in range(b-1,-1,-1):
                    massageCoder += keyCoder[i][j]
        if (key[0][1]=='4'):
            for i in range(a-1,-1,-1):
                for j in range(b-1,-1,-1):
                    massageCoder += keyCoder[i][j]   
    if (key[0][0]=='3'):
        if (key[0][1]=='1'):
            for i in range(0,b,1):
                for j in range(0,a,1):
                    massageCoder += keyCoder[j][i]
        if (key[0][1]=='2'):
            for i in range(b-1,-1,-1):
                for j in range(0,a,1):
                    massageCoder += keyCoder[j][i]  
    if (key[0][0]=='4'):
        if (key[0][1]=='1'):
            for i in range(0,b,1):
                for j in range(a-1,-1,-1):
                    massageCoder += keyCoder[j][i]
        if (key[0][1]=='2'):
            for i in range(b-1,-1,-1):
                for j in range(a-1,-1,-1):
                    massageCoder += keyCoder[j][i]
    coderMessage = "".join(massageCoder)
    print(coderMessage)

    return coderMessage

def startServer():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024)
            data = data.decode()
            data = data.split(" ",1)
            parsePackage(data[0],data[1])
                
if __name__ == '__main__':
    startServer()