import sys

def generatetestlinesphone():
    testlines = input("Test input : \n")

    lines = ""

    for line in testlines.strip().split("\n") :
        lines = lines + "\n\t\"" + line + "\\n\","

    lines = "\n\n\n#BEGINS\n tlos = [" + lines + "]\n\n#ENDS\n\n"

    print(lines)

def generatetestlinesmac():
    testlines = sys.stdin.readlines() # "Favourite foods followed by EOF:" User gives input... Ctrl+D
    lines = ""

    for line in testlines.strip().split("\n") :
        lines = lines + "\n\t\"" + line + "\\n\","

    lines = "\n\n\n#BEGINS\n tlos = [" + lines + "]\n\n#ENDS\n\n"

    print(lines)

#generatetestlinesmac()
generatetestlinesphone()