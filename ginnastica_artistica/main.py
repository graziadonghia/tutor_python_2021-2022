
from operator import itemgetter


FILENAME = "punteggi.txt"

def leggiPunteggi(filename):
    punteggiPerNazione = {}
    atlete = []
    try:
        f = open(filename, "r")
    except:
        print("Errore nell'apertura del file")

    for lineStr in f:
        line = lineStr.replace("\n", "").split(" ")
        nome = line[0]+line[1]
        sesso = line[2]
        nazione = line[3]
        voti = ricavaVotiValidi(line[4:])
        if nazione in punteggiPerNazione.keys():
            punteggiPerNazione[nazione] += sum(voti)
        else:
            punteggiPerNazione[nazione] = sum(voti)
        if sesso == "F":
            atlete.append((nome, nazione, sum(voti)))

    f.close()
    return atlete, punteggiPerNazione

def cercaVincitrice(atlete):
    vincitrice = atlete[0]
    maxPunteggio = vincitrice[2]
    for atleta in atlete:
        if atleta[2] > maxPunteggio:
            vincitrice = atleta
    return vincitrice

def ricavaVotiValidi(line):
    voti = [float(i) for i in line]
    voti.remove(max(voti))
    voti.remove(min(voti))
    return voti

def classificaNazioni(punteggiPerNazione):
    return sorted(punteggiPerNazione.items(), key=itemgetter(1), reverse=True)

def stampaClassifica(classifica):
    for i in range(0, len(classifica)):
        nazione = classifica[i]
        print(str(i)+"°) "+nazione[0]+" - Punteggio Finale: "+str(round(nazione[1], 1)))
def main():   
    atlete, punteggiPerNazione = leggiPunteggi(FILENAME) 
    vincitrice = cercaVincitrice(atlete)
    print("Vincitrice femminile:")
    print(vincitrice[0]+", "+vincitrice[1]+" - Punteggio: "+str(vincitrice[2]))
    print("Classifica complessiva nazioni:")
    classifica = classificaNazioni(punteggiPerNazione)
    stampaClassifica(classifica)

main()

