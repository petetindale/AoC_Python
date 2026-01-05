import numpy as np

VERBOSE = True


def top_k_closest_pairs(dist: np.ndarray, k: int):
  dist2 = dist.copy()
  
  # keep only upper triangle => unique undirected pairs (i < j)
  iu, ju = np.triu_indices(dist2.shape[0], k=1)
  d = dist2[iu, ju]                    # distances for unique pairs

  # sort unique pairs by distance
  order = np.argsort(d)
  order = order[:k]

  return iu[order], ju[order], d[order] 
  
def measuredistances(locs3ds:np.array):
    
  points = locs3ds.copy()
  
  # Pairwise differences (N x N x 3)
  diff = points[:, None, :] - points[None, :, :]
  
  # Pairwise distances (N x N)
  dist = np.linalg.norm(diff, axis=2)
  
  # Ignore self-distance
  np.fill_diagonal(dist, np.inf)
  
  return dist
  


class connectjunctions:
  def __init__(self, input_data:list):
    self.locations = np.array(list(map(lambda loc: list(map(lambda coord: int(coord), loc.split(","))), input_data)))
    
    self.distarray = measuredistances(self.locations)
    
    
    
    
    
  def bucketclosest(self, closestidx):
    buckets = list()
    
    for index, closest in enumerate(closestidx):
      
      all_items = set().union(*buckets)
      if {index, closest} & all_items:
        bucketidx = next((i for i, s in enumerate(buckets) if index in s), None)
        if bucketidx is not None:
          buckets[bucketidx].add(closest)
        else :
          bucketidx = next((i for i, s in enumerate(buckets) if closest in s), None)
          buckets[bucketidx].add(index)
          
      else :
        buckets.append({index,closest})
        
    print(buckets)
    
  
  
  


#Need this in each day
def run(part:int, input_data:list):
  print(f"Day 0 - Part {part}")
  print(f"---First line length = {len(input_data[0])}---")
  print(f"---Number of rows = {len(input_data)}---")
  
  
  junctions = connectjunctions(input_data)
  
  
  ans = 0
  if part == 1 :
    ans = 1
  else :
    ans = 0
  return ans
  
