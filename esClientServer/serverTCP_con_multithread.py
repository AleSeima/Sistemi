import socket as sck
from sys import float_repr_style
import threading as thr

class Client_Manager(thr.Thread):   #sottoclasse della cvlase madre Thread, quella in parentesi è la classe padre
    def __init__(self, connection, address):
        thr.Thread.__init__(self)   #super di Java, costruttore della classe madre
        self.connection = connection
        self.address = address
        self.running = True

    def run(self):  #contiene il codice del Thread
        while self.running: #ricevo i dati e li stampa
            recived_msg = self.connection.recv(4096)
            print(f"<{thr.current_thread}>Messaggio ricevuto{self.address}:  {recived_msg.decode()}")   #thr.current_thread: mi da il nome del thread che la sta chiamando

            for conn in self.connectionList:
                conn.sendall(recived_msg)    #rimanda il messaggio al client

            if recived_msg.decode().startswith("exit"):
                self.running = False
                self.connection.close()


def main():
    connectionList = []
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)    #SOCK_STREAM vuol dire TCP
    s.bind(('127.0.0.1', 5000))
    s.listen()  #alloca risosre sul server

    while True:
        connection, address = s.accept() #ritorna la connessione e l'indirizzo
        connectionList.append(connection)
        client = Client_Manager(connection, address)
        client.start()

        for conn in connectionList:
            if client.running == False:
                print("Chiuso")
                conn.join   #chiude il thread

if __name__ == '__main__':
    main()

#JOIN: metodo classe Thread: unisce il flusso di codice di un thread lo termina e riusnisce i flussi, se uso il join termina il thred e annulla il suo flusso, ma sarà il main thread che lo chiude
#Se accetto tante connessioni ho tante connessioni, per comunicare allo stesso tempo con piu connessioni come facio?
#Gestisco ogni client con un thread diverso, un thread dedicato0 a ogni client
#nel client ho input da tastiera e recezione fare un tread che riceve mex da socket e l'altro che li riceve da tastiera