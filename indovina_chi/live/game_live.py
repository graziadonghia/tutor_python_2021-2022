from characters_live import printCharacter

def matchOk(character, questions):
    for q in questions:
        prop = q[0]
        value = q[1]
        if character[prop] != value:
            return False

    return True

def play(filename, characters, properties):
    questions = [] 
    move = 0 #contatore delle mosse
    f = open(filename, "r")
    for lineStr in f:
        move += 1
        print("Mossa "+str(move)+" - domanda: "+lineStr)
        line = lineStr.replace("\r\n", "").split("=") 
        questions.append(line)
        print("Personaggi selezionati:")
        selected = 0
        #inizio la ricerca
        for c in characters:
            if matchOk(c, questions):
                selected += 1
                winner = dict(c) #possibile vincitore
                printCharacter(c, properties)
        print("\n")

    f.close()
    if selected == 1:
        print("Gioco terminato, hai vinto! E' stato selezionato:")
        printCharacter(winner, properties)
    else:
        print("Peccato, hai perso :(")