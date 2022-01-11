from histogram import buildHistogram
from histogram import readZodiac
PLAYERS = "sportivi.csv"
ZODIAC = "zodiaco.csv"
DEFAULT = 50


def main():
    zodiac = readZodiac(ZODIAC)
    histogram = buildHistogram(zodiac, PLAYERS)
    printOutput(histogram)


main()
