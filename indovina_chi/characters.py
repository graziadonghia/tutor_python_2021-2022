def printCharacter(character, properties):
    line = character["Nome"]+" - "
    for prop in properties:
        if character[prop] != "NO" and character[prop] != "SI":
            line = line+prop+": "+character[prop]+", "
        if character[prop] == "SI":
            line = line+prop
    print(line[:-2])

def saveCharacters(filename):
    characters = []

    f = open(filename, "r")
    for lineStr in f:
        line = lineStr.replace("\r\n", "").split(";")
        if line[0] == "Nome":
            #header
            properties = list(line)
        else:
            newCharacter = dict({k:v for k,v in zip(properties, line)})
            characters.append(newCharacter)
    
    f.close()
    return characters, properties
