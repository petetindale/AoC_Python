import numpy as np
import functools as fn
from operator import mul

VERBOSE = False


class ConnectJunctions:
  def __init__(self, input_data:list, n:int):
    self.locations = np.array(list(map(lambda loc: list(map(lambda coord: int(coord), loc.split(","))), input_data)))
    
    self.distarray = ConnectJunctions.measure_distances(self.locations)
    
    self.i, self.j, self.d = ConnectJunctions.top_n_closest_pairs(self.distarray, n)

    if VERBOSE : print(list(zip(self.i, self.j, self.d)))
    
    self.buckets, self.last = ConnectJunctions.bucket_closest(self.i, self.j, len(self.locations))

    if VERBOSE : print(self.buckets)

  def top_3_largest_buckets_lens_multiplied(self):
    return fn.reduce(mul, list(map(lambda b: len(b), self.buckets[:3])))
    
  def last_x_connected(self):
    if self.last != (0,0):
      a,b = self.last
      
      loca = self.locations[a]
      locb = self.locations[b]
      return loca[0] * locb[0]
    return 0

  @staticmethod
  def top_n_closest_pairs(dist: np.ndarray, n: int):
    dist2 = dist.copy()
    
    # keep only upper triangle => unique undirected pairs (i < j)
    iu, ju = np.triu_indices(dist2.shape[0], k=1)
    d = dist2[iu, ju]                    # distances for unique pairs

    # sort unique pairs by distance
    order = np.argsort(d)
    if n != -1 :
      order = order[:n]

    return iu[order], ju[order], d[order] 

  @staticmethod  
  def measure_distances(locs3ds:np.array):
      
    points = locs3ds.copy()
    
    # Pairwise differences (N x N x 3)
    diff = points[:, None, :] - points[None, :, :]
    
    # Pairwise distances (N x N)
    dist = np.linalg.norm(diff, axis=2)
    
    # Ignore self-distance
    np.fill_diagonal(dist, np.inf)
    
    return dist

  @staticmethod
  def bucket_closest(a:np.array, b:np.array, n:int):
      buckets = []
      last = (0,0)

      for x, y in zip(a, b):
          bx = next((k for k, s in enumerate(buckets) if x in s), None)
          by = next((k for k, s in enumerate(buckets) if y in s), None)

          if bx is None and by is None:
              buckets.append({x, y})
          elif bx is not None and by is None:
              buckets[bx].add(y)
          elif bx is None and by is not None:
              buckets[by].add(x)
          else:
              # both already in buckets
              if bx != by:
                  # merge by into bx (and delete the old bucket)
                  buckets[bx] |= buckets[by]
                  del buckets[by]
          
  
          
          if len(buckets) >= 1:
            if len(buckets[0]) == n:
              last = (x, y)
              break # all in the same bucket
          

      buckets.sort(key=len, reverse=True)
      
      if VERBOSE : print(last)

      return buckets, last

    
  

#Need this in each day
def run(part:int, input_data:list):
  print(f"Day 8 - Part {part}")
  print(f"---First line length = {len(input_data[0])}---")
  print(f"---Number of rows = {len(input_data)}---")

  n = 1000 if len(input_data) > 100 else 10 #yuk ... but not adding another var to the input process ... yet
  if part == 2 : n = -1 #all pairs

  junctions = ConnectJunctions(input_data, n)

  ans = 0
  if part == 1 :
    ans = junctions.top_3_largest_buckets_lens_multiplied()
  else :
    ans = junctions.last_x_connected()
  return ans
  
