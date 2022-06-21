import socket as socket
from dataclasses import dataclass
import numpy as np
from binascii import unhexlify
#import ModBusPackageSlave as ModBusPackage
import time
HOST = 'localhost'
PORT : int = 9090

@dataclass
class ModBusPackage:
    adM : np.uint8 #Адрес устройства
    funCode: np.uint8  #Функциональный код
    byteC: np.uint8 #Количество байт
    rVA0 : np.uint16 #Register value (AO0)
    rVA1 : np.uint16 #Register value (AO1)
    rVA2 : np.uint16 #Register value (AO2)
    crc: np.uint16 #CRC16

    def __init__(self, adM: np.uint8, funCode: np.uint8, byteC: np.uint8,rVA0 : np.uint16,rVA1 : np.uint16,rVA2 : np.uint16,crc: np.uint16):
        self.adM = adM
        self.funCode = funCode
        self.byteC = byteC
        self.rVA0 = rVA0
        self.rVA1 = rVA1
        self.rVA2 = rVA2
        self.crc = crc

    def toHexList(self):
        messageArray = []
        messageArray.append(hex(self.adM))
        messageArray.append(hex(self.funCode))
        messageArray.append(hex(self.byteC))
        messageArray.append(hex(self.rVA0))
        messageArray.append(hex(self.rVA1))
        messageArray.append(hex(self.rVA2))
        messageArray.append(hex(self.crc))
        return messageArray

    def checkCRC(message):
        lines = message.split(' ')
        if(lines[4]=="0x7687"):
            return True
        else:
            return False

p = ModBusPackage
p.__init__(p,17,3,6,44609,22098,17216,44361) # Create ModBusPackage
messageArray = ModBusPackage.toHexList(p)
print(messageArray)

def startServer():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((HOST,PORT))
    print(f'Listening at {HOST}:{PORT}')
    m=0
    tocMain = time.perf_counter()
    while True:
        msg = sock.recv(100)
        if(msg.decode("UTF-8")=="E"):
            break
        if(ModBusPackage.checkCRC(msg.decode("UTF-8"))):
            m+=1
    print("Количество принятых пакетов: ", m)
    ticMain = time.perf_counter()
    print(ticMain-tocMain)
    sock.close()

if __name__ == '__main__':
    startServer()