from os import path
import toml

def getpath(levels:int, year:int, day:int):
  return path.dirname(__file__) + ("/.."*levels + "/inputs/") + f"{year}/day{day}/"
  

def getlos(pathdir:str, test:bool):
    #set input path 
    input_path = pathdir 
    data_filename = "input.txt"
    testdata_filename = "testinput.txt"
    input_filename = testdata_filename if test else data_filename
    #Load file information
    f = open(input_path + input_filename, "r")
    list_of_strings = f.readlines()
    f.close()
    return list_of_strings
 
def gettests(pathdir:str, year:int, day:int):
  tests = toml.load(pathdir+"testanswers.toml")
  return tests
  
