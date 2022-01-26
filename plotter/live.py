N = 5
riquadro = [] #matrice inizializzata a lista vuota

def inizializzaMatrice():
    for i in range(N):
        riga = ["."]*N
        riquadro.append(riga)

def stampaMatrice():
    for i in range(N):
        for j in range(N):
            print(riquadro[i][j], end=" ")
        print("\n")

def convertiRiga(riga):
    return N - riga - 1

def disegnaPunto(row, col):
    riquadro[row][col] = "*"

def disegnaRigaOrizzontale(row, col, length):
    for j in range(col, col+length -1):
        if riquadro[row][j] == "|":
            riquadro[row][j] = "+"
        else:
            riquadro[row][j] = "-"

def disegnaRigaVerticale(row, col, length):
    #for che decrementa l'indice delle righe
    for i in range(row, row-length-1, -1):
        if riquadro[i][col] == "-":
            riquadro[i][col] = "+"
        else:
            riquadro[i][col] = "|"

def main():
    inizializzaMatrice()
    stampaMatrice()
    try:
        f = open("plotter.txt", "r")
    except IOError:
        exit("Errore nell'apertura del file")
    
    for record in f:
        campi = record.strip().split(" ")
        i = convertiRiga(int(campi[1]))
        j = int(campi[2])

        if campi[0] == "P":
            disegnaPunto(i, j)
        if campi[0] == "H":
            l = int(campi[3])
            disegnaRigaOrizzontale(i, j, l)
        if campi[0] == "V":
            l = int(campi[3])
            disegnaRigaVerticale(i, j, l)
    f.close()

    stampaMatrice()





main()

