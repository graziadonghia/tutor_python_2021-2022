
def convertiData(data):
    giorno = data.split("/")[0]
    mese = data.split("/")[1]
    return mese+giorno

def leggiZodiaco():
    segniZodiacali = [] #chiavi del dizionario
    durate = [] #valori del dizionario
    try:
        f = open("zodiaco.csv")
    except IOError:
        exit("Errore nell'apertura del file")

    for record in f:
        line = record.strip().split(",")
        segniZodiacali.append(line[0])
        dataInizio = convertiData(line[1])
        dataFine = convertiData(line[2])
        durate.append((dataInizio, dataFine))
    f.close()

    zodiaco = dict({k:v for k,v in zip(segniZodiacali, durate)})
    
    return zodiaco

def trovaSegnoZodiacale(dataNascita, zodiaco):
    for segno in zodiaco.keys():
        intervallo = zodiaco[segno]
        if dataNascita >= intervallo[0] and dataNascita <= intervallo[1]:
            return segno

def ordinaIstogramma(istogramma):
    istogrammaLista = []
    for k in istogramma.keys():
        coppia = (istogramma[k], k)
        istogrammaLista.append(coppia)
    
    istogrammaLista.sort(reverse=True)
    
    return istogrammaLista

def stampaIstogramma(istogrammaOrdinato):
    maxTupla = istogrammaOrdinato[0]
    maxGol = maxTupla[0]

    for coppia in istogrammaOrdinato:
        segno = coppia[1]
        numGol = coppia[0]
        numAsterischi = (50*numGol)//maxGol
        print(segno+" "+"("+str(numGol)+")  "+numAsterischi*"*")

def main():
    zodiaco = leggiZodiaco()
    # for k in zodiaco.keys():
    #     print(k+": "+str(zodiaco[k]))
    istogramma = dict({k:0 for k in zodiaco.keys()})

    try:
        f = open("sportivi.csv")
    except IOError:
        exit("Errore nell'apertura del file")
    
    for record in f:
        line = record.strip().split(",")
        numGol = int(line[1])
        dataNascita = convertiData(line[3])
        segno = trovaSegnoZodiacale(dataNascita, zodiaco)
        istogramma[segno] += numGol
    
    f.close()

    istogrammaOrdinato = ordinaIstogramma(istogramma)
    stampaIstogramma(istogrammaOrdinato)




main()

