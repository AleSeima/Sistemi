#creare un programma che prenda un messaggio da un compagno e la mandi ad un altro

import socket as sck

def main():
    s= sck.socket(sck.AF_INET, sck.SOCK_DGRAM) #istanzia una socket

    s.bind(("192.168.0.123", 7000)) #serve solo ne server, nella tupla c'è il nome del server e la porta a scelta (deve essere maggiore di 1024)
    #ss.encode serve per convetire una stringa in binario, perchè i socket possono inviare e riceve solo questo tipo di stringhe 
    while True:
        data, addr = s.recvfrom(4096) #è la funzione per ricevere, restituisce il dato inviato e una tupla, che contiene l'indirizzo inviato e la porta
        #s.sendto(data, addr)#è la funzione per inviare pacchetti, contiene una stringa binaria, e un indirizo(tupla) del ricevente
        s.sendto(data,("192.168.0.126", 7000))#è la funzione per inviare pacchetti, contiene una stringa binaria, e un indirizo(tupla) del ricevente
        data.decode()
        print(data)

if __name__=="__main__":
    main()