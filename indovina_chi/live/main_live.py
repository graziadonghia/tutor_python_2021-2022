CHARACTERS_FILENAME = "personaggi.txt"
QUESTIONS_FILENAME = "domande2.txt"

from characters_live import saveCharacters, printCharacter
from game_live import play

def main():
    characters, properties = saveCharacters(CHARACTERS_FILENAME)
    print("Personaggi del gioco:")
    for c in characters:
        printCharacter(c, properties[1:])
    print("\n\n")
    play(QUESTIONS_FILENAME, characters, properties)


main()