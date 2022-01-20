from operator import itemgetter


FILENAME = "fantacalcio.txt"

def scegliCalciatore(ruolo, calciatori, budget, num, squadra):
    listaCalciatori = calciatori[ruolo] #lista di tuple (cognome, quotazione)
    for calciatore in sorted(listaCalciatori, key=itemgetter(1), reverse=True):
        cognome, quotazione = calciatore
        if quotazione <= budget and budget - quotazione > num:
            squadra[ruolo].append((cognome, quotazione))
            budget -= quotazione
            num -= 1
            if num == 0:
                #ho scelto tutti i calciatori che mi servivano per quel ruolo
                break
        
def formaSquadra(calciatoriPerRuolo, budgetPerRuolo, numPerRuolo, ruoli):
    squadra = dict({k:[] for k in ruoli})
    for ruolo in ruoli:
        #scelgo calciatori per ruolo
        #verifico se mi rimane budget
        scegliCalciatore(ruolo, calciatoriPerRuolo, budgetPerRuolo[ruolo], numPerRuolo[ruolo], squadra)
        if budgetPerRuolo[ruolo] > 0:
            budgetPerRuolo[ruolo] = 0
    
    return squadra

def salvaDatiFantacalcio(filename, ruoli):
    calciatoriPerRuolo = dict({k:[] for k in ruoli}) #inizializzo solo le chiavi
    #inizialmente i valori sono liste vuote
    try:
        f = open(filename, "r")

    except:
        print("Errore nell'apertura del file")

    for lineStr in f:
        line = lineStr.replace("\n", "").split(", ")
        #line[0] = cognome
        #line[2] = ruolo
        #line[3] = quotazione stringa
        cognome = line[0]
        ruolo = line[2]
        quotazione = int(line[3]) 
        calciatoriPerRuolo[ruolo].append((cognome, quotazione))
    
    f.close()

    return calciatoriPerRuolo

def main():
    ruoli = ["portiere", "difensore", "centrocampista", "attaccante"] #chiavi
    quotazioni = [20, 40, 80, 120] #valori
    num = [3, 8, 8, 6] #valori

    budgetPerRuolo = dict({k:v for k,v in zip(ruoli, quotazioni)})
    numPerRuolo = dict({k:v for k,v in zip(ruoli, num)})
    
    calciatoriPerRuolo = salvaDatiFantacalcio(FILENAME, ruoli) #dizionario con calciatori non ordinati per quotazione

    squadra = formaSquadra(calciatoriPerRuolo, budgetPerRuolo, numPerRuolo, ruoli)

    #stampa squadra 
    for ruolo in ruoli:
        print(ruolo.capitalize()[:-1]+"i: ", end=" ")
        for calciatore in squadra[ruolo]:
            print(calciatore[0]+" "+str(calciatore[1]), end=" ")
        print("\n")


main()
