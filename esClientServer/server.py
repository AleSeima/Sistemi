import socket as sck

def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
    s.bind(('localhost', 5000))

    while True:
        data, addr = s.recvfrom(4096)   #restituisce il messaggio, e l'IP dell'altra macchina chde lo ha mandato
        s.sendto(data, addr)
        print(data)


if __name__ == '__main__':
    main()