class rangeid:
  def __init__(self, rng:list):
    self.fromstr = rng[0]
    self.fromint = int(self.fromstr)
    self.tostr = rng[1]
    self.toint = int(self.tostr)
  
  def findinvalid(self, mod2plus:bool):
    suminv = 0
    for i in range(self.fromint, self.toint+1):
      cstr = str(i)
      clen = len(cstr)
      if clen%2 == 0 and not mod2plus:
        if cstr[:clen//2] == cstr[clen//2:]:
          print(i)
          suminv += i
      elif mod2plus :
        found = 0
        for seq in list(range(1, clen, 1)):
          if clen % seq == 0 :
            sumseq = [cstr[j:j+seq] for j in range(0, clen, seq)]
            if len(set(sumseq)) <= 1 :
              found += 1
              
        if found > 0:
          suminv += i
            
        
    return suminv
 


def sumallinvalid(numrange:list, mod2plus:bool):
  suminv = 0
  for rng in numrange:
    suminv += rng.findinvalid(mod2plus)
  return suminv


def parsestring(input_data:list):
  nums = list(map(lambda x : rangeid(x.split("-")), input_data[0].split(",")))
  return nums


#Need this in each day
def run(part:int, input_data:list):
  print(f"Day 2 - Part {part}")
  nums = parsestring(input_data)
  ans = 0
  if part == 1 :
    ans = sumallinvalid(nums, False)
  else :
    ans = sumallinvalid(nums, True)
  return ans
  
  
  #horizontal = fn.reduce(lambda x, y : x + y.horizontal(), move_list, horizontal)
