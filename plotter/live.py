NOME_FILE = "plotter.txt"
N = 5
riquadro = [] #inizializzo matrice di puntini

def inizializzaMatrice():
    for i in range (N):
        row = ["."]*N
        riquadro.append(row)
    
def stampaMatrice():
    for row in range(0, N):
        for col in range(0, N):
            print(riquadro[row][col], end=" ")
        print("\n")

def convertiRighe(row): #corretta
    return N-row-1

def disegnaPunto(x, y):
    riquadro[x][y] = "*"

def disegnaRigaOrizzontale(xIn, yIn, l):
    for j in range(yIn, yIn+l-1):
        if riquadro[xIn][j] == "|":
            riquadro[xIn][j] = "+"
        else:
            riquadro[xIn][j] = "-"

def disegnaRigaVerticale(xIn, yIn, l):
    for i in range(xIn, xIn-l-1, -1):
        if riquadro[i][yIn] == "-":
            riquadro[i][yIn] = "+"
        else:
            riquadro[i][yIn] = "|"

def main():
    inizializzaMatrice()
    try:
        f = open(NOME_FILE, "r")
    except IOError:
        exit("Errore nell'apertura del file")

    for lineStr in f:
        line = lineStr.strip().split(" ")
        #print(line[1]+" "+line[2]+"--->", end=" ")
        x = convertiRighe(int(line[1])) #riga
        y = int(line[2])
        #print(str(x)+" "+str(y))
        if line[0] == "P":
            disegnaPunto(x, y)
        elif line[0] == "H":
            l = int(line[3])
            disegnaRigaOrizzontale(x, y, l)
        elif line[0] == "V":
            l = int(line[3])
            disegnaRigaVerticale(x, y, l)
        
    f.close()
    stampaMatrice()

main()