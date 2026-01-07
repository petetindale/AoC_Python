import numpy as np

VERBOSE = False

class FloorTiles:
  def __init__(self, input_data:list):
    self.red_tiles = np.array(list(map(lambda loc: list(map(lambda coord: int(coord), loc.split(","))), input_data)))

    #Get leftmost, rightmost, topmost, bottommost
    self.min_x = np.min(self.red_tiles[:,0])
    self.min_idx = np.argmin(self.red_tiles[:,0])
    self.max_x = np.max(self.red_tiles[:,0])
    self.max_idx = np.argmax(self.red_tiles[:,0])
    self.min_y = np.min(self.red_tiles[:,1])
    self.min_idy = np.argmin(self.red_tiles[:,1])
    self.max_y = np.max(self.red_tiles[:,1])
    self.max_idy = np.argmax(self.red_tiles[:,1])


  def largest_area(self):
    
    return 0
    


#Need this in each day
def run(part:int, input_data:list):
  print(f"Day 9 - Part {part}")
  print(f"---First line length = {len(input_data[0])}---")
  print(f"---Number of rows = {len(input_data)}---")

  if VERBOSE : print(f"Input Data: {input_data}")

  floortiles = FloorTiles(input_data)

  ans = 0
  if part == 1 :
    ans = floortiles.largest_area()
  else :
    ans = 0
  return ans
  
