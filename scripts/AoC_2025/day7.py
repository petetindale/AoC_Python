import numpy as np



class tachmap:
  START = 9
  SPLITTER = 1
  EMPTY = 0
  
  @staticmethod
  def parsechars(ele:str):
    match (ele):
      case 'S':
        return tachmap.START
      case '.':
        return tachmap.EMPTY
      case '^':
        return tachmap.SPLITTER
  
  def __init__(self, mapstrs:list):
    self.time = 0
    
    self.tm = np.matrix(list(map(lambda line : list(map(tachmap.parsechars, line)), mapstrs)))
    #print(self.tm)
    
    self.beammap = np.where(self.tm==9,1,0)
    #print(self.beammap)
    
    
  #got lost in the matrix. chatgpt helped...
  def movebeam(self):
    tmap = (self.tm == 1)          # boolean mask
    nrows, ncols = self.beammap.shape

    row = 1
    countsplits = 0
    
    while self.beammap[-1].sum() == 0 and row < nrows:
        # 1) copy down into THIS row only (where previous row is non-zero)
        prev = self.beammap[row - 1]
        mask_down = prev != 0
        self.beammap[row, mask_down] = prev[mask_down]

        # snapshot AFTER copy-down (prevents cascading within this step)
        tbeams = self.beammap.copy()
        rowarr = self.beammap[row]    
        trow   = tbeams[row]
        
        # 2) outward copy ONLY on THIS row, only where tmap is true and value != 0
        src_row = tmap[row] & (tbeams[row] != 0)   # shape: (ncols,)

        idx = np.flatnonzero(src_row)

        # copy to left (j -> j-1), ignore j=0
        j = idx[idx > 0]
        rowarr[j - 1] = trow[j]
        
        # copy to right (j -> j+1), ignore j=last
        j = idx[idx < (len(rowarr) - 1)]
        rowarr[j + 1] = trow[j]
        
        rowarr[idx] = 0
        
        
        countsplits += len(idx)
    
        row += 1

    #print(self.beammap)
    return countsplits
 
  def paths(self):
    tmap = (self.tm == 1)    # boolean mask
    nrows, ncols = self.beammap.shape
    
    tpaths = np.zeros_like(self.beammap) # empty to count
    
    tbeams = self.beammap.copy() #dont want to change
    
    row = nrows - 2
    
    tpaths[nrows - 1] = tbeams[nrows - 1]
    
    while row >= 0 :
      beneath = tpaths[row+1]
      tmask = (tbeams[row] == 1)

      currow = tpaths[row]
      
      currow[tmask] = beneath[tmask]
      
      
      si = np.flatnonzero(tmap[row])
      
      
      currow[si]=beneath[si-1]+beneath[si+1]
      
      
      row -= 1
    
    #print(tpaths)
    return tpaths[0].sum()
  
  
  '''
  #my attempt.
  def movebeam(self):
    tmap = np.where(self.tm==1,1,0)
    print(tmap)
    
    row = 1
    
    while self.beammap[-1].sum() == 0 :
      #copy line above if not zero
      mask = self.beammap[row-1] != 0
      self.beammap[row][mask]=self.beammap[row-1][mask]
      
      tbeams = self.beammap.copy()
      
      src = tmap & (tbeams !=0)
      
      print("before")
      print(tbeams)
      
      print(src)
      
      # copy to left neighbour (j-1) from source (j)
      self.beammap[:, :-1][src[:, 1:]] = tbeams[:, 1:][src[:, 1:]]

      # copy to right neighbour (j+1) from source (j)
      self.beammap[:, 1:][src[:, :-1]] = tbeams[:, :-1][src[:, :-1]]
      
      self.beammap[src] = 0
      
      print(f"after {row}")
      print(self.beammap)
      
      
      row += 1
      
    
    
    print(self.beammap)
  '''  

#Need this in each day
def run(part:int, input_data:list):
  print(f"Day 7 - Part {part}")
  print(f"---First line length = {len(input_data[0])}---")
  print(f"---Number of rows = {len(input_data)}---")
  tachm = tachmap(input_data)
  splits = tachm.movebeam()
  ans = 0
  if part == 1 :
    ans = splits
  else :
    ans = tachm.paths()
  return ans
  
