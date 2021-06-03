import socket as sck
import threading as thr
import time

clientList = [] #lista dei client

class Client_Manager(thr.Thread):
    def __init__(self, connection, nickname, destinatario):   #costruttore
        thr.Thread.__init__(self)   #costruttore super (java)
        self.connection = connection
        self.nickname = nickname
        self.destinatario = destinatario
        self.running = True

    def run(self):  #fin che esiste il Thread
        while self.running: #fin che esiste il Thread
            receivedMessage = self.connection.recv(4096)    #riceve il messaggio

            if receivedMessage.decode() == "exit":     #se il messaggio ricevuto inizia con EXIT fa terminare il programma, chiude tutto sia server che tutti i client connessi
                self.running = False
                time.sleep(0.01)
                break

            else:
                print(f"<{thr.current_thread()}> Messaggio ricevuto da {self.nickname.decode()}: {receivedMessage.decode()}")   #stampa: nickname: messaggio, inviati dal client

                receivedMessage = self.nickname.decode() + ":" + receivedMessage.decode()   #trsformo in stringa e modifico per aggiunere cio che voglio

                for client in clientList:   #per rimandare il messaggio a tutti i client connessi al server
                    '''if client.nickname != self.nickname:      '''  #per non rimandare il messaggio a chi lo ha mandato e scritto
                    if client.nickname == self.destinatario:        #per mandare il messaggio solo al mittente
                        client.connection.sendall(receivedMessage.encode())  #per ogni thread collegato a questo server manda il messaggio ricevuto, ritraformo in binario

def main():
    print(f"Io sono {thr.current_thread()}")   #stampa codice identificativo macchina
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)    #creo un nuovo socket
    s.bind(("127.0.0.1", 7000))     #specifica la porta a cui si deve connettere, e con l'IP della mia macchina
    s.listen()      #in ascolto di messaggi da client

    global clientList       #in quanto deve essere visibile in tutto il programma

    dizUsers = {}       #associo il nickname alla tupla

    while True:
        connection, address = s.accept()       #in s.accept() ci sono connection e address

        #Ricezione del nickname
        nickname = connection.recv(4096)        #recezione messaggio
        destinatario = connection.recv(4096)
        dizUsers[nickname.decode()] = (destinatario, address)       #mette nel dizionario il nome come chiave, e la tupla come valore della chiave
        print(dizUsers) 

        client = Client_Manager(connection, nickname, destinatario)   #viene creato il Thread, ogni thread corrisponde a un client
        clientList.append(client)   #aggiungo alla lista di Thread il nuovo client
        client.start()  #viene startato il Thread

        for client in clientList:
            if client.running == False:
                print("Chiusura")
                client.connection.close()   #PER CHIOUDERE CONESSIONE, NELLA FUNZ ANCHE IL SOCKET
                client.join()
                clientList.remove(client)

if __name__ == '__main__':
    main()