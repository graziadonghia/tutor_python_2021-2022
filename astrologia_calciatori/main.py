PLAYERS = "sportivi.csv"
ZODIAC = "zodiaco.csv"

def retrieveDate(string):
    dateList = string.replace("\r\n","").split("/")
    date = dateList[1] + dateList[0]
    return date 
    
def readZodiac(filename):
    zodiac = {}
    f = open(filename, "r")
    for line in f:
        dates = {}
        lineList = line.split(",")
        sign = lineList[0]
        start = retrieveDate(lineList[1])
        end = retrieveDate(lineList[2])
        dates.update({"start": start, "end": end})
        zodiac.update({sign: dates})
    f.close()
    return zodiac

def buildHistogram(zodiac, playersFilename):
    histogram = dict.fromkeys(zodiac,0)
    f = open(playersFilename, "r")
    for line in f:
        #name surname,numGol,nationality,birthDate
        lineList = line.split(",") 
        numGol = int(lineList[1]) #2nd element of the list
        birthDate = retrieveDate(lineList[3])
        for sign in zodiac.keys():
            signDates = zodiac[sign].values()
            if birthDate >= signDates[0] and birthDate <= signDates[1]:
                histogram[sign] += numGol
    f.close()
    return histogram

def main():
    players = readPlayers(PLAYERS)
    zodiac = readZodiac(ZODIAC)
    #print("PLAYERS")
    #print(players)
    #print("ZODIAC")
    #print(zodiac)
    histogram = buildHistogram(zodiac, PLAYERS)
    print(histogram)

main()