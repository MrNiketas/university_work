import socket as sc
import threading
import time

N = 5000


def threadSocket(sock):
    tik = time.perf_counter()
    t = 5
    for i in range(1, N):
        if i == N - 2:
            time.sleep(5)
            continue
        if i == N - 1:
            sock.sendto(b'E', ('127.0.0.1', 9090))
            t = t / i / 2
            time.sleep(t)
        sock.sendto(b'TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT', ('127.0.0.1', 9090))
        t = t / i * 8
        time.sleep(t)
    tok = time.perf_counter()
    print(tok - tik)


def start_client():
    sock = sc.socket(sc.AF_INET, sc.SOCK_DGRAM)
    th = threading.Thread(target=threadSocket(sock))

    th.start()


if __name__ == '__main__':
    start_client()