import socket as socket
from dataclasses import dataclass
import numpy as np
import time

@dataclass
class ModBusPackage:
    adM : np.uint8
    funCode: np.uint8
    rVA0 : np.uint16
    rV : np.uint16
    crc: np.uint16

    def __init__(self, adM: np.uint8, funCode: np.uint8,rVA0 : np.uint16,rV : np.uint16,crc: np.uint16):
        self.adM = adM
        self.funCode = funCode
        self.rVA0 = rVA0
        self.rV = rV
        self.crc = crc

    def toHexList(self):
        messageArray = []
        messageArray.append(hex(self.adM))
        messageArray.append(hex(self.funCode))
        messageArray.append(hex(self.rVA0))
        messageArray.append(hex(self.rV))
        messageArray.append(hex(self.crc))
        return messageArray

    def checkCRC(message):
        if(message[6]==0xad49):
            return True

N = 1000000
p = ModBusPackage
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
p.__init__(p,17,3,107,3,30343) # Create ModBusPackage
messageArray = ModBusPackage.toHexList(p)
str = ""
for i in messageArray:
    str += i+" "
print(str)
t = 1
for i in range(1,N):
    if(i==N-2):
        time.sleep(3)
        sock.sendto(bytes("E","UTF-8"),('127.0.0.1',9090))
    sock.sendto(bytes(str,"UTF-8"),('127.0.0.1',9090))
    t = t/i
    time.sleep(t)