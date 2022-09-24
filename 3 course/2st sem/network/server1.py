import socket as sc
import threading
from threading import Thread
import time
import matplotlib.pyplot as plot
import numpy as np
#while True:
#   try:
#        client,addr = sock.accept()
#        print("РћРїР°! РќРѕРІС‹Р№ РєР»РёРµРЅС‚! РџРѕ Р°РґСЂРµСЃСѓ: ", addr)
#   except KeyboardInterrupt:
#        sock.close()
 #       print("РЎРµСЂРІРµСЂ СѓРјРµСЂ...")
 #       break
#   else:
def threadByte():
    sock = sc.socket(sc.AF_INET,sc.SOCK_DGRAM)
    sock.bind(('127.0.0.1',9090))
    print("Р’С‹ СЃРѕР·РґР°Р»Рё UDP СЃРµСЂРІРµСЂ!")
    package = 0
    PointsPackage = []
    PointsTime = []
    tocMain = time.perf_counter()
    while True:
        package1 = 0
        tic = time.perf_counter()
        data = sock.recv(50)
        if(data.decode("utf-8") == "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"):
            package += 1.0
            package1 += 1.0
        if(data.decode("utf-8")=="E"):
            package +=1.0
            package1 +=1.0
            break
        print("РџР°РєРµС‚ РІ РёС‚РµСЂР°С†РёРё",package)
        toc = time.perf_counter()
        ti = toc- tic
        print("Р’СЂРµРјСЏ РёС‚РµСЂР°С†РёРё:",ti)
        PointsPackage.append(package1)
        PointsTime.append(ti)
    ticMain = time.perf_counter()
    print("Р’СЂРµРјСЏ РїРѕРґРєР»СЋС‡РµРЅРёСЏ:",ticMain-tocMain)
    plot.autoscale(True)
    plot.plot(PointsPackage,PointsTime)
    plot.show()

th = Thread(threadByte())
th.start()