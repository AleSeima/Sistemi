def main():
    pila = [] #lista vuota
    ok = True
    stringa = input("inserisci una stringa con parentesi: ")

    for lettera in stringa: #scorre i caratteri della stringa
        if lettera == '(' or lettera == '[' or lettera == '{':      #se legge una aperta
            pila.append(lettera)    #push, prende la ( e la matte al fondo della pila
        elif lettera == ')':    #elseif se è una chiusa, fa la pop, e toglie dalla pila l'ultimo elemento
            #if pila.pop() != NULL:
            if pila.pop() != '(':       #qui la pop funziona al contrario, prende l'ultimo elemento della pila
                ok = False
                break
        elif lettera == ']':
            #if pila.pop() != NULL:
            if pila.pop() != '[':
                ok = False
                break
        elif lettera == '}':
            #if pila.pop() != NULL:
            if pila.pop() != '{':
                ok = False
                break

    if ok == True:
        print("Ordine parentesi corretto")
    else:
        print("Ordine parentesi errato")

if __name__ == "__main__":
    main()