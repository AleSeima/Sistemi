import socket as sck

def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)

    while True:
        messaggio = input("Inserire il messaggio desiderato:")
        s.sendto(messaggio.encode(), ("192.168.0.117", 5500))    #funzione per inviare i pacchetti contiene la stringa binaria che è il messaggio e l'indirizzo che sarebbe la tupla: (IP del sever, e la porta del server)
        #data, addr = s.recvfrom(4096)   #è la funzione per ricevere, restituisce il dato inviato e una tupla: (IP e PORTA del server), restituisce il messaggio, e l'IP dell'altra macchina chde lo ha mandato
        

if __name__ == '__main__':
    main()
# per mandare stringhe dentro un soket prima le converto in binario ss.encode