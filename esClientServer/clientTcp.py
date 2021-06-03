import socket as sck

def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.connect(('localhost', 5000))
    print("Connessione avvenuta")

    while True:
        messaggio = input("Inserire il messaggio desiderato:")  #riga blocante 
        s.sendall(messaggio.encode())
        if messaggio == "exit":
            print("Chiusura connessione")
            break
        data = s.recv(4096)     #riga bloccante, 4096 NON è la porta
        print(f"Messaggio dal server: {data.decode()}")
    s.close()

if __name__ == '__main__':
    main()
# per mandare stringhe dentro un soket prima le converto in binario ss.encode