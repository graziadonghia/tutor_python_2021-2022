# coding= UTF-8
FILENAME = "fantacalcio.txt"

import random
def sceltaCalciatoriPerRuolo(ruolo, calciatori, budgetPerRuolo, numPerRuolo, squadra):

    for c in calciatori[ruolo]:
        cognome, quotazione = c
        if int(quotazione) <= budgetPerRuolo[ruolo] and budgetPerRuolo[ruolo] - int(quotazione) > numPerRuolo[ruolo]:
            squadra[ruolo].append((cognome, quotazione.replace("\n", "")))
            budgetPerRuolo[ruolo] -= int(quotazione)
            numPerRuolo[ruolo] -= 1
            if numPerRuolo[ruolo] == 0:
                break 

def salvaDatiFantacalcio(filename, ruoli):
    #dizionario con tutti i calciatori
    #il ruolo è la chiave e il valore è una lista di calciatori, ogni calciatore è una tupla (cognome, ruolo, quotazione)
    calciatori = dict({k:[] for k in ruoli})
    try:
        f = open(filename)
    except:
        print("Errore nell'apertura del file")
    
    for lineStr in f:
        line = lineStr.replace("\r\n", "").split(", ")
        #line[0] = cognome
        #line[2] = ruolo
        #line[3] = quotazione
        calciatori[line[2]].append((line[0], line[3]))

    f.close()
    # print("Elenco calciatori:")
    # for k in calciatori.keys():
    #     print(k)
    #     for c in calciatori[k]:
    #         print(c)
    #     print("\n")
    return calciatori

def formaSquadra(ruoli, calciatori, budgetPerRuolo, numPerRuolo):
    squadra = dict({k:[] for k in ruoli})
    for ruolo in ruoli:
        random.shuffle(calciatori[ruolo]) #randomize - optional
        sceltaCalciatoriPerRuolo(ruolo, calciatori, budgetPerRuolo, numPerRuolo, squadra)
        #scelgo di azzerare il budget se avanzato
        if budgetPerRuolo[ruolo] > 0:
            budgetPerRuolo[ruolo] = 0

    return squadra

def main():
    ruoli = ["portiere", "difensore", "centrocampista", "attaccante"]
    quotazioni = [20, 40, 80, 120]
    num = [3, 8, 8, 6]
    budgetPerRuolo = dict({k:v for k,v in zip(ruoli, quotazioni)}) #value = int
    numPerRuolo = dict({k:v for k,v in zip(ruoli, num)}) #value = int
    # print(budgetPerRuolo)
    # print(numPerRuolo)
    calciatori = salvaDatiFantacalcio(FILENAME, ruoli)
    squadra = formaSquadra(ruoli, calciatori, budgetPerRuolo, numPerRuolo)

    #controlli su tot calciatori e tot budget non messi
    
    #stampa squadra scelta
    for ruolo in ruoli:
        print(ruolo.capitalize()[:-1]+"i: ", end= " ")
        for c in squadra[ruolo]:
            print(c[0]+" "+c[1], end=" ")
        print("\n")
        

main()
