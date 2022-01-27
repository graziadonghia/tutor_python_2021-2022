mappa = []
def stampaMappa():
    numRow = len(mappa)
    for i in range(numRow):
        numCol = len(mappa[i])
        for j in range(numCol):
            print(mappa[i][j], end=" ")
        print("\n")

def salvaMappa(filename):
    try:
        f = open(filename, "r")
    except IOError:
        exit("Errore nell'apertura del file")
    
    for line in f:
        record = line.strip().split(" ") #lista di stringhe
        row = [int(num) for num in record]
        numCol = len(row)
        mappa.append(row)
    
    numRow = len(mappa)
    f.close()

    return numRow, numCol

def cimaNonCasoLimite(val, i, j):
    if val == 0:
        return False
    if mappa[i-1][j] > val or mappa[i+1][j] > val or mappa[i][j-1] > val or mappa[i][j+1] > val or mappa[i-1][j-1] > val or mappa[i+1][j-1] > val or mappa[i+1][j+1] > val or mappa[i-1][j+1] > val:
        return False
    return True

def cimaPrimaRiga(val, i, j, numRow, numCol):
    if val == 0:
        return False
    #distinguo i casi in cui mi trovo nella prima colonna o nell'ultima
    if j == 0:
        #sono nell'angolo in alto a sx
        if mappa[i][j+1] > val or mappa[i+1][j+1] > val or mappa[i+1][j] > val:
            return False
        return True
    
    if j == numCol - 1:
        #sono nell'angolo in alto a dx
        if mappa[i][j-1] > val or mappa[i+1][j-1] > val or mappa[i+1][j] > val:
            return False
        return True
    
    #se sono arrivata qui non sono mai uscita dalla funzione
    #caso "standard" 
    if mappa[i][j-1] > val or mappa[i+1][j-1] > val or mappa[i+1][j] > val or mappa[i+1][j+1] > val or mappa[i][j+1] > val:
        return False
    return True

def cimaUltimaRiga(val, i, j, numRow, numCol):
    if val == 0:
        return False
    if j == 0:
        #sono nell'angolo in basso a sx
        if mappa[i-1][j] > val or mappa[i-1][j+1] > val or mappa[i][j+1] > val:
            return False
        return True
    
    if j == numCol - 1:
        #sono nell'angolo in basso a dx
        if mappa[i-1][j] > val or mappa[i-1][j-1] > val or mappa[i][j-1] > val:
            return False
        return True
    
    #caso "standard"
    if mappa[i-1][j] > val or mappa[i-1][j-1] > val or mappa[i][j-1] > val or mappa[i-1][j+1] > val or mappa[i][j+1] > val:
        return False
    return True

def cimaPrimaColonna(val, i, j, numRow, numCol):
    if val == 0:
        return False
    if i == 0:
        #sono nell'angolo in alto a sx
        if mappa[i][j+1] > val or mappa[i+1][j+1] > val or mappa[i+1][j] > val:
            return False
        return True
    if i == numRow - 1:
        #sono nell'angolo in basso a sx
        if mappa[i-1][j] > val or mappa[i-1][j+1] > val or mappa[i][j+1] > val:
            return False
        return True
    
    #caso standard
    if mappa[i-1][j] > val or mappa[i-1][j+1] > val or mappa[i][j+1] > val or mappa[i+1][j+1] > val or mappa[i+1][j] > val:
        return False
    return True

def cimaUltimaColonna(val, i, j, numRow, numCol):
    if val == 0:
        return False
    if i == numRow - 1:
        #sono nell'angolo in basso a dx
        if mappa[i-1][j] > val or mappa[i-1][j-1] > val or mappa[i][j-1] > val:
            return False
        return True
    if i == 0:
        #sono nell'angolo in alto a dx
        if mappa[i][j-1] > val or mappa[i+1][j-1] > val or mappa[i+1][j] > val:
            return False
        return True
    #caso "standard"
    if mappa[i-1][j] > val or mappa[i-1][j-1] > val or mappa[i][j-1] > val or mappa[i+1][j-1] > val or mappa[i+1][j] > val:
        return False
    return True

def calcolaAltezzaMedia(cime):
    somma = sum(cime)
    count = len(cime)
    avg = somma/count
    return avg



def main():
    numRow, numCol = salvaMappa("mappa.txt")
    #stampaMappa()
    cime = []
    trovata = False
    #cerco le cime nella matrice
    for i in range(numRow):
        for j in range(numCol):
            val = mappa[i][j] 
            if i == 0:
                trovata = cimaPrimaRiga(val, i, j, numRow, numCol)
            elif i == numRow - 1:
                trovata = cimaUltimaRiga(val, i, j, numRow, numCol)
            elif j == 0:
                trovata = cimaPrimaColonna(val, i, j, numRow, numCol)
            elif j == numCol - 1:
                trovata = cimaUltimaColonna(val, i, j, numRow, numCol)
            else:
                trovata = cimaNonCasoLimite(val, i, j)
            
            if trovata:
                cime.append(val)
                print(str(val)+" "+str(i)+" "+str(j))
    if len(cime) > 0:
        avg = calcolaAltezzaMedia(cime)
        print("Altezza media : "+str(avg)+ " m")
    else:
        print("Non ci sono cime")


main()