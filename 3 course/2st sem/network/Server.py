import socket
import zlib
import matplotlib.pyplot as plt


def can_receiver(client_data):
    secs = 0.1
    speed = 0
    allPackets = 0
    lostPackets = 0
    Packets = 0
    list_lost_packets = list()
    list_speed = list()
    while allPackets <= 230:
        allPackets += 1
        Packets += 1
        can_array = bytearray(client_data.recv(1024))
        try:
            client_hash = can_array.pop()
            server_hash = ""
            for sym in str(zlib.crc32(can_array)):
                if len(server_hash) != 2:
                    server_hash += sym
            if client_hash == int(server_hash):
                print("Пакетов принято: ", allPackets, "| Пакетов потеряно: ", lostPackets)
                print("Задержка ", int(secs * 1000), "мс\n")
            else:
                print("!!!!!!!!!!!!!Пакет поврежден!!!!!!!!!!!!!!\n")
                lostPackets += 1
                print("Пакетов принято: ", allPackets, "| Пакетов потеряно: ", lostPackets)
                print("Задержка ", int(secs * 1000), "мс\n")
            if Packets == 3:
                secs -= 0.001
                speed += 0.3
                Packets = 0
            list_lost_packets.append(lostPackets)
            list_speed.append(int(secs * 1000))
        except:
            print("Пакет потерялся\n")
            lostPackets += 1
            print("Пакетов принято: ", allPackets, "| Пакетов потеряно: ", lostPackets)
            print("Задержка ", int(secs * 1000), "мс\n")
            list_lost_packets.append(lostPackets)
            list_speed.append(int(secs * 1000))
    print(list_lost_packets)
    print(list_speed)
    return list_speed, list_lost_packets


def plotting(cords_x, cords_y):
    fig, ax = plt.subplots()
    ax.plot(cords_x, cords_y,color='green')
    ax.set_xlabel("мс")
    ax.set_ylabel("Потерянные пакеты")
    plt.show()

def connection():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 51017))
    server.listen(True)
    print("Сервер ожидает подключение клиента")
    client_data, client_address = server.accept()
    print("Клиент подключен ", client_address)
    list_cords_x, list_cords_y = can_receiver(client_data)
    plotting(list_cords_x, list_cords_y)
    client_data.close()

SERVER = socket.gethostbyname(socket.gethostname())
print(f"[LISTENING] Server is listening on {SERVER}")
connection()





