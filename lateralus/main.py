FILENAME = "lateralus.txt"

def storeAlbum(filename):
    album = {}
    f = open(filename, "r")
    num = 1
    for song in f:
        album[num] = song
        num += 1
    f.close()
    return album

def storeAlbumPro(filename):
    f = open(filename, "r")
    return f.read()

def stereo():
    album = storeAlbum(FILENAME)
    num = input("Which song do you want to listen? ")
    while (num != "stop"):
        num = int(num)
        if num in album.keys():
            print(album[num])
        else:
            print("Wrong song number: this album has "+ str(len(list(album.keys())))+" songs")
        num = input("Which song do you want to listen? ")

def countSize(album):
    count = 1 #number of songs
    for i in album:
        if i == '\n':
            count += 1
    size = 1
    while album[size] != '\n':
        size += 1
    size += 1 #include '\n'

    return count, size

def stereoPro():
    album = storeAlbumPro(FILENAME)
    count, size = countSize(album)
    offset = 0
    #album is a string
    num = input("Which song do you want to listen? ")
    while (num != "stop"):
        num = int(num)
        if num <= count and num != 0:
            start = (num-1)*size
            end = start + size
            print(album[start:end])
        else:
            print("Wrong song number: this album has "+ str(count)+" songs")
        num = input("Which song do you want to listen? ")


def main():
    pro = False
    if pro:
        stereoPro()
    else:
        stereo()
main()