#putting files in file

def gettingLinks():
    numOfLinks = int(input("How many links do you want to put in the file: "))

    f = open("linksForYoutube.txt", "w")
    for x in range(numOfLinks):
        currentLink = input("Please put a link into the file: ")
        f.write(currentLink + '\n')

    f = open("linksForYoutube.txt", "r")
    nice = f.read().splitlines()
    return nice
