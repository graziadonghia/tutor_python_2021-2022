FILE_PRODOTTI = "prodotti.txt"
FILE_ACQUISTI = "acquisti.txt"

def salvaProdotti(filename):
    prodIDs = [] #ID dei prodotti
    vendorIDs = [] #ID dei rivenditori ufficiali
    try:
        f = open(filename, "r")
    except:
        print("Errore nell'apertura del file")
    
    for line in f:
        lineList = line.replace("\n", "").split(" ")
        #lineList[0] = productID
        #lineList[1] = vendorID
        prodIDs.append(lineList[0]) #key
        vendorIDs.append(lineList[1])
    f.close()

    #costruisco dizionario
    prodAndVend = dict({k:v for k,v in zip(prodIDs, vendorIDs)})
    
    return prodAndVend

def controlloAcquisti(filename, prodAndVend):
    prodIDs = [] #key
    vendIDs = [] #value
    sospetti = []

    try:
        f = open(filename, "r")
    except:
        print("Errore nell'apertura del file")
    
    for line in f:
        lineList = line.replace("\n", "").split(" ")
        #lineList[0] = prod ID
        #lineList[1] = vendor ID
        prod = lineList[0]
        vend = lineList[1]
        prodIDs.append(prod)
        vendIDs.append(vend)

        if vend != prodAndVend[prod]:
            #sospetto trovato
            sospetti.append(prod)
        f.close()
    
    #costruisco dizionario degli acquisti
    acquisti = dict({k:v for k,v in zip(prodIDs, vendIDs)})

    return acquisti, sospetti

def main():
    prodAndVend = salvaProdotti(FILE_PRODOTTI)
    print(prodAndVend)

    acquisti, sospetti = controlloAcquisti(FILE_ACQUISTI, prodAndVend)

    print("Elenco transazioni sospette")

    for s in sospetti: #s è una chiave 
       print("Codice prodotto: "+s) 
       print("Rivenditore ufficiale: "+prodAndVend[s])
       print("Lista rivenditori: "+str(acquisti[s]))
       print("\n")

main()