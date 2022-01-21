FILE_PEDAGGI = "pedaggi.txt"
FILE_PERCORSI = "percorsi.txt"

def leggiPedaggi():
    ingressi = []
    uscite = []
    pedaggi = []

    #apro file pedaggi
    try:
        f = open(FILE_PEDAGGI, "r")
    except IOError:
        exit("Errore nell'apertura del file")
    
    #leggo file pedaggi
    for lineStr in f:
        line = lineStr.strip().split(";")
        ingressi.append(line[0])
        uscite.append(line[1])
        pedaggi.append(float(line[2]))
    f.close()

    return ingressi, uscite, pedaggi

def leggiPercorsi():
    partenze = []
    arrivi = []

    try:
        f = open(FILE_PERCORSI, "r")
    except IOError:
        exit("Errore nell'apertura del file")
    
    for lineStr in f:
        line = lineStr.strip().split(";")
        partenze.append(line[0])
        arrivi.append(line[-1])
        
    f.close()

    return partenze, arrivi


def main():

    ingressi, uscite, pedaggi = leggiPedaggi()
    partenze, arrivi = leggiPercorsi()
    importiPagati = [0]*len(arrivi) 
    #controllo preliminare: verifico che la partenza sia in ingressi e che l'arrivo sia in uscite
    for partenza, arrivo in zip(partenze, arrivi):
        #partenza e arrivo iterano parallelamente nelle due liste 
        trovato = False #flag per vedere se il percorso esiste
        count = 0 #contatore delle successioni di caselli
        if partenza in ingressi and arrivo in uscite:
            #potrebbe esistere un percorso
            tempCaselloPartenza = partenza #variabile temporanea
            while count < len(ingressi):
                index = ingressi.index(tempCaselloPartenza)
                tempCaselloArrivo = uscite[index]
                count += 1
                importiPagati[index] += pedaggi[index]
                if tempCaselloArrivo == arrivo:
                    trovato = True
                    break #esci dal while
                else :
                    tempCaselloPartenza = tempCaselloArrivo 
            if trovato:
                print("Percorso "+partenza+"-"+arrivo+": "+str(count)+" caselli, tariffa totale "+str(importiPagati[index]))
        else:
            print("Percorso "+partenza+"-"+arrivo+": non raggiungibile")



main()


