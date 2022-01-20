
from operator import itemgetter

FILENAME = "punteggi.txt"


def convertToFloatAndNormalize(listaPunti):
    puntiFloat = [float(punto) for punto in listaPunti]

    #rimuovo max e min
    puntiFloat.remove(max(puntiFloat))
    puntiFloat.remove(min(puntiFloat))

    return puntiFloat

def leggiPunteggi(filename):

    atlete = []
    puntiPerNazione = {}

    try:
        f = open(filename, "r")
    except:
        print("Errore nell'apertura del file")
    
    for lineStr in f:
        line = lineStr.replace("\n", "").split(" ") #lista di stringhe
        nome = line[0] + line[1] #nome e cognome
        genere = line[2]
        nazione = line[3]
        punteggi = convertToFloatAndNormalize(line[4:])

        if genere == "F":
            atlete.append((nome, nazione, sum(punteggi)))
        
        if nazione in puntiPerNazione.keys():
            puntiPerNazione[nazione] += sum(punteggi)

        else:
            puntiPerNazione[nazione] = sum(punteggi)
         
    f.close()

    return atlete, puntiPerNazione

def trovaVincitrice(atlete):
    vincitrice = atlete[0] #(nome, nazione, punteggio)
    maxValue = vincitrice[2]

    for atleta in atlete:
        if atleta[2] > maxValue:
            vincitrice = atleta
    
    return vincitrice

def stampaClassificaNazioni(newPuntiPerNazione):
    #punti per nazione è una lista di tuple
    #[("ITA", 55.9), ("USA", 52.2),...]
    posto = 1
    for punteggio in newPuntiPerNazione:
        nazione = punteggio[0]
        punteggio = punteggio[1]
        print(str(posto)+"°) "+nazione+" - Punteggio Finale: "+str(round(punteggio, 1)))
        posto += 1
        if posto > 3:
            break
    
def classificaNazioni(puntiPerNazione):
    return sorted(puntiPerNazione.items(), key=itemgetter(1), reverse=True)


def main():

    atlete, puntiPerNazione = leggiPunteggi(FILENAME)
    vincitrice = trovaVincitrice(atlete)
    #vincitrice[0] = nome
    #vincitrice[1] = nazione
    #vincitrice[2] = punteggio

    print("Vincitrice femminile:")
    print(vincitrice[0]+", "+vincitrice[1]+" - Punteggio: "+str(vincitrice[2]))

    newPuntiPerNazione = classificaNazioni(puntiPerNazione)

    print("Classifica complessiva nazioni:")
    stampaClassificaNazioni(newPuntiPerNazione)



main()
