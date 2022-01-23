FILE_ARTISTI = "artisti.txt"

def getBandFiles(filename):
    #legge il file "artisti.txt"
    #ritorna un dizionario con codice:nomeFile
    bandFiles = {}
    try:
        f = open(filename, "r")
    except IOError:
        exit("Errore nell'apertura del file")
    
    #i codici sono univoci nel file
    for record in f:
        line = record.strip().split(";")
        code = line[0]
        bandFile = line[1]
        bandFiles[code] = bandFile
    
    f.close()
    return bandFiles

def storeSongInformation(bandFiles):
    #caricare le informazioni relative a tutti i brani di tutti gli artisti

    #due dizionari: 
    #{artista:[(anno, canzone)]}
    # {anno:[(canzone, band)]}

    songsPerBand = {}
    songsPerYear = {}

    for bandCode in bandFiles.keys():
        filename = bandFiles[bandCode]

        try:
            f = open(filename, "r")
        except IOError:
            exit("Errore nell'apertura del file "+filename)

        #inizializzo lista di canzoni della band a lista vuota
        songsPerBand[bandCode] = []
        

        for record in f:
            line = record.strip().split(";")
            year = line[0]
            song = line[1]
            songsPerBand[bandCode].append((year, song))
            if year in songsPerYear.keys():
                songsPerYear[year].append((song, bandCode))
            else:
                songsPerYear[year] = [] #inizializzo lista vuota
                songsPerYear[year].append((song, bandCode))

        f.close()
    return songsPerBand, songsPerYear

def printOutput(songsPerYear):
    for year in sorted(songsPerYear.keys()):
        print(year+":")
        for songBand in songsPerYear[year]:
            song = songBand[0]
            bandCode = songBand[1]
            print(song+"\t"+bandCode)
    
def main():
    bandFiles = getBandFiles(FILE_ARTISTI)
    #print(bandFiles)
    songsPerBand, songsPerYear = storeSongInformation(bandFiles)
    #print(songsPerBand)
    #print(songsPerYear)
    printOutput(songsPerYear)

main()
    