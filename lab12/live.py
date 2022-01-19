FILE_PRESENZE = "presenze.txt"
FILE_SOSPETTI = "sospetti.txt"
#salva il contenuto di presenze.txt 
def salvaFile(filename1, filename2):
    presenze = {}
    sospetti = []
    try:
        f1 = open(filename1, "r")
    except:
        print("Errore nell'apertura del file 1")

    try:
        f2 = open(filename2, "r")
    except: 
        print("Errore nell'apertura del file 2")
    
    for lineStr in f1:
        line = lineStr.replace("\n", "").split(",")
        nome = line[0]
        tel = line[1]
        arrivo = line[2]
        partenza = line[3]

        presenze[nome] = (tel, arrivo, partenza)

    for lineStr in f2:
        sospetti.append(lineStr.replace("\n", ""))
    
    f1.close()
    f2.close()

    return presenze, sospetti
def contattoSospettoInsiemi(arrivo, partenza, conArrivo, conPartenza):
    setSospetto = set()
    setContatto = set()

    #costruisco intervallo temporale sospetto
    for i in range(int(arrivo), int(partenza)+1):
        setSospetto.add(i)
    
    #costruisco intervallo temporale contatto
    for i in range(int(conArrivo), int(conPartenza)+1):
        setContatto.add(i)

    setIntersezione = setSospetto.intersection(setContatto)
    if len(setIntersezione) != 0:
        return True
        
    return False
def contattoSospetto(arrivo, partenza, conArrivo, conPartenza):
    if ((conArrivo > arrivo and conArrivo < partenza) or (conArrivo < arrivo and conPartenza > arrivo)):
        return True
    return False 
def cercaSospetti(nome, presenze):
    setContattiSospetti = set()
    count = 0 #contatore sospetti
    (tel, arrivo, partenza) = presenze[nome]
    print("** Contatti del cliente "+nome+": **")
    for contatto in presenze.keys():
        (conTel, conArrivo, conPartenza) = presenze[contatto]
        if contatto != nome:
            if contattoSospettoInsiemi(arrivo, partenza, conArrivo, conPartenza):
                count += 1
                setContattiSospetti.add(contatto)
    if count == 0:
        print("Il cliente non ha avuto contatti sospetti")
    else:
        #stampa insieme di contatti
        for contatto in sorted(setContattiSospetti):
            telefono, arrivo, partenza = presenze[contatto]
            print("Contatto con "+contatto+", telefono: "+telefono)
    print("\n")

def main():
    presenze, sospetti = salvaFile(FILE_PRESENZE, FILE_SOSPETTI)
    for nome in sospetti: #lista di sospetti
        if nome in presenze.keys():
            cercaSospetti(nome, presenze)
        else:
            print("Cliente "+nome+" non presente in arichivio")


main()