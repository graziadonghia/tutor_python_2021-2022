import sys

def valid_format(line):
    #expected types: str; str; float; date

    #check if there are 4 fields
    if len(line) != 4:
        return "file format error: expected 4 fields in line, got "+str(len(line))
    if type(line[0]) != str or type(line[1]) != str or type(line[2]) != float:
        return "file format error: wrong type of fields in line"
    return ""

def main():
    errmsg = ""
    dict = {}
    filename = sys.argv[1]
    f = open(filename, "r")
    for line in f:
        #type(line) = str
        line_list = line.split(";")
        #name;service;cost;date
        line_list[2] = float(line_list[2])
        #print(line_list)
        err = valid_format(line_list)
        if err != "":
            print(err)
            sys.exit(-1)
        service = line_list[1]
        cost = line_list[2]
        if service in dict.keys():
            dict[service] = dict[service] + cost
        else:
            dict[service] = cost
    f.close()
    print(dict)
main()