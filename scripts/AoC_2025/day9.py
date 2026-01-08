import numpy as np
from itertools import combinations

VERBOSE = True

class FloorTiles:
  def __init__(self, input_data:list):
    self.red_tiles = np.array(list(map(lambda loc: list(map(lambda coord: int(coord), loc.split(","))), input_data)))
      
    self.areas = FloorTiles.all_areas_with_index(self.red_tiles)
    
    self.areas.sort(key=lambda x:x[2], reverse=True)
    
    
    if VERBOSE : print(self.areas)

  def largest_area(self):
    if len(self.areas) > 0:
      return self.areas[0][2]
    return 0
  
  @staticmethod
  def calculate_area(posa, posb):
    ax, ay = posa
    bx, by = posb
    
    lenx = abs(ax-bx)+1
    leny = abs(ay-by)+1
    
    return lenx * leny
  
  @staticmethod
  def all_areas_with_index(points):
    # returns (i, j, area)
    return [(i, j, FloorTiles.calculate_area(points[i], points[j])) for i, j in combinations(range(len(points)), 2)]
    


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
  
