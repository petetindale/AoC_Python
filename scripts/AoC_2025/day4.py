import numpy as np

def adjacent_sum(mat):
    padded = np.pad(mat, 1)
    return (
        padded[:-2, :-2] + padded[:-2, 1:-1] + padded[:-2, 2:] +
        padded[1:-1, :-2]                  + padded[1:-1, 2:] +
        padded[2:, :-2] + padded[2:, 1:-1] + padded[2:, 2:]
    )

def createrollsmat(rolls:list):
  rollsmat = np.matrix(list(map(lambda roll: list(map(lambda x: 1 if x == '@' else 0, roll)), rolls)))
  return rollsmat

def findadjacent(rolls:np.matrix):  
  summat = adjacent_sum(rolls)
  matched = np.where(rolls==1,summat,0)
  rollsmatch = np.where(matched<4,rolls,0)
  return rollsmatch

def removerolls(rolls:np.matrix):
  total = 0
  removable = 1
  tmp_rolls = rolls
  while removable != 0 :
    possiblerolls = findadjacent(tmp_rolls)
    removable = np.sum(possiblerolls)
    tmp_rolls = tmp_rolls - possiblerolls
    total += removable
  return total
  

#Need this in each day
def run(part:int, input_data:list):
  print(f"Day 4 - Part {part}")
  print(f"---First line length = {len(input_data[0])}---")
  rolls = createrollsmat(input_data)
  ans = 0
  if part == 1 :
    ans = np.sum(findadjacent(rolls))
  else :
    ans = removerolls(rolls)
  return ans
  
