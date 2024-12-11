from os import path

def getlos(input_filename):
    #set input path 
    input_path = path.dirname(__file__) + ("/../inputs/")
    #Load file information
    f = open(input_path + input_filename, "r")
    list_of_strings = f.readlines()
    f.close()
    return list_of_strings
