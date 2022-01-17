from characters import printCharacter

def matchOk(character, questions):
    for question in questions:
        prop = question[0]
        value = question[1]
        if character[prop] != value:
            return False
    return True

def play(filename, characters, properties):
    questions = [] #list of questions
    move = 0 #moves counter
    f = open(filename, "r")
    for lineStr in f:
        move += 1
        print("Mossa "+str(move)+" - domanda: "+lineStr)
        selected = 0 #selected characters
        line = lineStr.replace("\r\n", "").split("=")
        questions.append(list(line))
        print("Personaggi selezionati:")
        selected = 0
        for character in characters:
            if matchOk(character, questions):
                selected += 1
                winner = dict(character) #possible winner
                printCharacter(character, properties)
        print("\n")
    f.close()
    print("\n")
    if selected == 1:
        print("Gioco terminato, hai vinto! E' stato selezionato:")
        printCharacter(winner, properties)
    else:
          print("Peccato, hai perso :-(")
