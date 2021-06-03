import socket as sck
import threading as thr

clientList = [] #lista dei client

class Client_Manager(thr.Thread):
    def __init__(self, s):   #costruttore
        thr.Thread.__init__(self)   #costruttore super (java)
        self.s = s
        recivedMessage, indirizzo = s.recvfrom(4096) #riceve il primo messaggio che mando
        self.indirizzo = indirizzo
        self.running = True

    def run(self):  #fin che esiste il Thread
        while self.running: #fin che esiste il Thread
            receivedMessage, indirizzo = self.s.recvfrom(4096)    #riceve il messaggio

            if receivedMessage.decode() == "exit":     #se il messaggio ricevuto inizia con EXIT fa terminare il programma, chiude tutto sia server che tutti i client connessi
                self.running = False   
                break

            else:
                print(f"<{thr.current_thread()}> Messaggio ricevuto: {receivedMessage.decode()}")   #stampa: nickname: messaggio, inviati dal client

                receivedMessage =  receivedMessage.decode()   #trsformo in stringa e modifico per aggiunere cio che voglio

                '''for client in clientList:   #per rimandare il messaggio a tutti i client connessi al server
                    if client.nickname != self.nickname:       #per non rimandare il messaggio a chi lo ha mandato e scritto
                    if client.nickname == self.destinatario:     '''
                self.s.sendto(receivedMessage.encode(), self.indirizzo)  #per ogni thread collegato a questo server manda il messaggio ricevuto, ritraformo in binario

def main():
    print(f"Io sono {thr.current_thread()}")   #stampa codice identificativo macchina
    s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)    #creo un nuovo socket
    s.bind(("localhost", 6000))     #specifica la porta a cui si deve connettere, e con l'IP della mia macchina

    global clientList       #in quanto deve essere visibile in tutto il programma

    dizUsers = {}       #associo il nickname alla tupla

    while True:

        #Ricezione del nickname
        #nickname, indirizzo = s.recvfrom(4096)  #restituisce sia dato che indirizzo
        #destinatario, indirizzo = s.recvfrom(4096)
        #dizUsers[nickname.decode()] = indirizzo      #mette nel dizionario il nome come chiave, e la tupla come valore della chiave
        #print(dizUsers) 

        client = Client_Manager(s)   #viene creato il Thread, ogni thread corrisponde a un client
        clientList.append(client)   #aggiungo alla lista di Thread il nuovo client
        client.start()  #viene startato il Thread

        for client in clientList:
            if client.running == False:
                print("Chiusura")
                client.s.close()
                client.join()
                clientList.remove(client)

if __name__ == '__main__':
    main()

#COSA SI FA QUABDO SI USANO I SOCKET