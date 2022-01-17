CHARACTERS_FILENAME = "personaggi.txt"
QUESTIONS_FILENAME = "domande1.txt"
from characters import printCharacter, saveCharacters
from game import play
def main():
    characters, properties = saveCharacters(CHARACTERS_FILENAME)
    print("Personaggi del gioco:")
    for c in characters:
        printCharacter(c, properties[1:])
    print("\n\n")
    play(QUESTIONS_FILENAME, characters, properties)
    

main()