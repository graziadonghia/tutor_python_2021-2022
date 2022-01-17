'''Modulo per salvare in una lista di dizionari i personaggi del gioco'''

def printCharacter(character, properties):
    line = character["Nome"]+" - "
    for prop in properties:
        #caso generale: stampo prop: value
        if character[prop] != "SI" and character[prop] != "NO":
            line = line + prop + ": "+character[prop]+", "
        if character[prop] == "SI":
            line = line + prop+", "
        
    print(line)


def saveCharacters(filename):
    characters = [] #lista di dizionari

    f = open(filename, "r")
    for lineStr in f:
        line = lineStr.replace("\r\n", "").split(";") 
        #controllo se sto leggendo l'header
        if line[0] == "Nome":
            properties = list(line) 
        else:
            character = dict({k:v for k,v in zip(properties, line)})
            characters.append(character)
    f.close()

    return characters, properties
