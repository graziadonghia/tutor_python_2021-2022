
from prop import proportion


def printOutput(histogram):
    values = histogram.items()
    values.sort(key=lambda x: x[1], reverse=True)
    maxTuple = values[0]
    maxValue = maxTuple[1]
    for tup in values:
        sign = tup[0]
        numAsterix = proportion(DEFAULT, maxValue, tup[1])
        outputLine = sign + " " + "(" + str(tup[1]) + ")" + numAsterix*"*"
        print(outputLine)
