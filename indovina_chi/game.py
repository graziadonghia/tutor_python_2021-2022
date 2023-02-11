from characters import printCharacter

def matchOk(character, questions):
    print(character)
    for question in questions:
        prop = question[0] # chiave
        value = question[1] # valore 
        if character[prop] != value: # se il personaggio non corrisponde alla caratteristica
            return False # ritorna falso
    return True # ritorna vero

def play(filename, characters, properties): # parametri = nome file domande
                                            # lista dizionari con personaggi
                                            # lista caatteristiche 
    questions = [] #list of questions
    move = 0 #moves counter
    f = open(filename, "r")
    for lineStr in f:
        move += 1
        print("Mossa "+str(move)+" - domanda: "+lineStr)
        selected = 0 #selected characters
        line = lineStr.replace("\n", "").split("=")
        questions.append((line[0], line[1]))
        # print(line)
        print("Personaggi selezionati:")
        selected = 0 # contatore dei personaggi che corrispondono
    
    f.close()
    print(questions)
    for character in characters: # itero nella lista di dizionari
        if matchOk(character, questions): # se il personaggio risponde
                                            # alle caratteristiche della domande
            selected += 1 # incremento il numero di personaggi selezionati 
            winner = character #possible winner
            printCharacter(character, properties)
    print("\n")
    print("\n")
    if selected == 1:
        print("Gioco terminato, hai vinto! E' stato selezionato:")
        printCharacter(winner, properties)
    else:
          print("Peccato, hai perso :-(")
