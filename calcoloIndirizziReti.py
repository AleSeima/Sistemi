#creare un programma cge prenda in input dall'utente un indirizzo IP e la subnet mask
#il programma deve calcolarel'indirizzo di broadcast e gli indirizzi utilizzabii

def stampaIpDisponibili(nSottoreti, ip, mask):
    nSottoretiBianrio = bin(nSottoreti)[2:]
    bitSottorete = len(str(nSottoretiBianrio))
    bitHost = 32-mask-bitSottorete  #3

    nHost = 2**(bitHost)

    for sottorete in range (nSottoreti):
        for host in range(2**(bitHost)):    #da zero a 8
            print(ip[:mask]+bin(sottorete)[2:].zfill(bitSottorete)+bin(host)[2:].zfill(bitHost))
        print("altraSottorete")

def main():
    ip = "192.168.100.0"
    mask = 26 #/26
    bit_di_host = 32 - mask
    ip_binario = ""
    for gruppo in ip.split("."):
        x = bin(int(gruppo))[2:] #da decimale puntato a binario
        x = x.zfill(8)  #riempie di zero gli spazi vuoti
        ip_binario = ip_binario + x
    print(f"Indirizzo ip di rete in binario: {ip_binario}")
    ip_broadcast_binario = ip_binario[:mask] + "1"*bit_di_host  #ind sottorete
    print(f"Indirizzo ip di broadcast in binario: {ip_broadcast_binario}")
    ip_broadcast = ""
    for i in range(0,32,8):
        gruppo = ip_broadcast_binario[i:i+8]
        ip_broadcast =  ip_broadcast + str(int(gruppo,2))+"."   #converte da binario a decimale con il ":2"
    ip_broadcast = ip_broadcast[:-1]    #per togliere l'ultimo punto dall ip
    print(f"Indirizzo ip di braodcast in decimale: {ip_broadcast}")

    nSottoreti = 5

    stampaIpDisponibili(nSottoreti, ip_binario, mask)


if __name__=="__main__":
    main()