def dequeque():
    return queque.pop(0)

def enqueque(queue, elemnt):
    queue.append(elemnt)

def main():
    coda = ["a", "b", "c", "d"]
    enqueque(coda, "z")
    print(coda)
    x = dequeque( )   #toglie il primo elemento della coda, quindi a
    print(x)
    print(coda)

if __name__ == "__main__":
    main()