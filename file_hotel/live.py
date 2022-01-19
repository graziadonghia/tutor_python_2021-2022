FILENAME = "sales.txt"


def controlloRiga(line):
  if len(line) != 4:
    #ritorna un messaggio di errore
    return "Errore nella riga del file. Richiesti 4 campi"
  if type(line[2]) != float:
    return "Errore nella riga del file. Importo deve essere float"
  
  return ""

def main():
  importiPerServizi = {}
  errmsg = ""

  try:
    f = open(FILENAME, "r")
  except:
    print("Errore nell'apertura del file")

  for lineStr in f:
    line = lineStr.replace("\n", "").split(";")
    #line[0] = nome
    #line[1] = servizio
    #line[2] = importo
    #line[3] = data
    # print(line)
    line[2] = float(line[2])
    errmsg = controlloRiga(line)
    if errmsg != "":
      print(errmsg)

    servizio = line[1]
    importo = line[2]

    #distinguo caso in cui incontro chiave per la prima volta --> inizializzo valore
    #non è la prima volta --> incremento valore
    if servizio in importiPerServizi.keys():
      #incremento
      importiPerServizi[servizio] = importiPerServizi[servizio] + importo
    else:
      #inizializzo
      importiPerServizi[servizio] = importo
    
  f.close()
  print(importiPerServizi)
  
main()