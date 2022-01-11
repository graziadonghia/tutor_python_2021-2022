def retrieveDate(string):
    dateList = string.replace("\r\n", "").split("/")
    date = dateList[1] + dateList[0]
    return date
