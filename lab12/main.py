#salvare il contenuto di presenze.txt --> eventuali contatti sospetti
def saveFiles(filename1, filename2):
    suspects = []
    presences = {} 

    try:
        f1 = open(filename1, "r")
    except:
        print("Problem in open file 1")
    

    try:
        f2 = open(filename2, "r")
    except:
        print("Problem in open file 2")

    for lineStr in f1:
        line = lineStr.replace("\r\n", "").split(",")
        key = line[0]
        tel = line[1]
        start = line[2]
        end = line[3]

        presences[key] = (tel, start, end)

    for lineStr in f2:
        suspects.append(lineStr.replace("\r\n", ""))

    f1.close()
    f2.close()
    return presences, suspects

def isSupectContact(n_start, n_end, p_start, p_end):
    set_n = set() 
    set_p = set() 
    for i in range(int(n_start), int(n_end) + 1):
        set_n.add(i)
    for i in range(int(p_start), int(p_end) + 1):
        set_p.add(i)
    
    set_intersection = set_n.intersection(set_p)
    if len(set_intersection) != 0:
        return True
    return False

def searchSuspetcs(name, presences):
    count = 0
    for p in sorted(presences):
        n_tel, n_start, n_end = presences[name]
        if p != name:
            p_tel, p_start, p_end = presences[p]
            if isSupectContact(n_start, n_end, p_start, p_end):
                count += 1
                print("Contatto con "+p+", numero: "+p_tel)
    if count == 0:
        print("Il cliente non ha avuto contatti sospetti")

def main():
    presences, suspects = saveFiles("presenze.txt", "sospetti.txt")
    print(presences)
    print(suspects)
    for s in suspects:
        name = s.replace("\n", "")
        if name in presences:
            (tel, start, end) = presences[name]
            print("** Contatti del cliente "+name+": **")
            searchSuspetcs(name, presences)
        else:
            print("Cliente "+name+" non presente in archivio")


main()