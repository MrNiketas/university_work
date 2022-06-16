import socket
import time
import threading
from threading import Thread

sock = socket.socket()
sock.connect(('localhost', 9090))
N = 1000

def thread_socket():
    i = 5
    for t in range(1,N):
        i = i/t
        byte = bytes("HelloWorld","utf-8")
        sock.send(byte)
        print("РџРѕС‚РѕРє Р·Р°СЃС‹РїР°РµС‚ РЅР° СЃРµРєСѓРЅРґ.", i)
        time.sleep(i)
        print("РџРѕС‚РѕРє СЃРµР№С‡Р°СЃ РїСЂРѕСЃРЅСѓР»СЃСЏ." )

def start_socket():
    th = Thread(target=thread_socket())
    while True:
        print("РџРѕС‚РѕРє СЂР°Р±РѕС‚Р°РµС‚")
        if th.is_alive:
            sock.close()
            print("Socket close")
            break

if __name__ == '__main__':
    start_socket()