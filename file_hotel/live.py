import sys

FILENAME = "sales.txt"

def valid_format(line):
  if len(line) != 4:
    return "file format error: expected 4 fields in line, got "+str(len(line))
  if type(line[0]) != str or type(line[1]) != str or type(line[2]) != float:
    return "file format error: wrong type of fields in line"
  return ""

def main():
  dict = {}
  f = open(FILENAME, "r")
  for line in f:
    line_list = line.split(";")
    line_list[2] = float(line_list[2])
    err = valid_format(line_list)
    if err != "":
      print(err)
      sys.exit(-1)
    service = line_list[1] #key
    cost = line_list[2]
    if service in dict.keys():
      dict[service] = dict[service] + cost
    else:
      dict[service] = cost

  f.close()
  print("total amount for each service: ")
  print(dict)

    
    

main()
    
  