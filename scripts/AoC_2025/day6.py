import functools as fn
from operator import mul

class mathprob :
  def __init__(self, opstr:str, start, end, numstr:list):
    self.oper = opstr
    #print(f"{self.oper}, {start}, {end}")
    self.nums = list()
    for ns in numstr :
      self.nums.append(int(ns[start:end+1]))
    
    self.altnums = list()
    for i in range(end, start-1, -1):
      curstr = ""
      for ns in numstr :
        curstr += ns[i]
      if curstr.strip() != "" :
        self.altnums.append(int(curstr.strip()))
  
  def swap(self):
    tmp = self.nums
    self.nums = self.altnums
    self.altnums = tmp
        
   
  @property 
  def total(self):
    if self.oper == "+":
      return sum(self.nums)
    else :
      return fn.reduce(mul, self.nums)
      
  def __add__(self, mp2):
    return self.total + mp2.total

  def __radd__(self, other):
    return self.total + other
    
def processmathshw(worksheet:list):
  opstr = worksheet[-1]
  numstrs = worksheet[:-1]
  
  start = 0
  end = -1
  curop = ""
  
  mathprobs = list()
  
  for i in range(len(opstr)) :
    if opstr[i] == "*" or opstr[i] == "+":
      if end != -1 : #ignore start
        mathprobs.append(mathprob(curop,start,end,numstrs))
      
      curop = opstr[i]
      start = i
    else:
      end = i
   
  if end != -1:
    #add last 
    mathprobs.append(mathprob(curop,start,end,numstrs))
      
  return mathprobs

#Need this in each day
def run(part:int, input_data:list):
  print(f"Day 6 - Part {part}")
  print(f"---First line length = {len(input_data[0])}---")
  print(f"---Number of rows = {len(input_data)}---")
  mathprobs = processmathshw(input_data)
  ans = 0
  if part == 1 :
    ans = sum(mathprobs)
  else :
    for mp in mathprobs:
      mp.swap()
    ans = sum(mathprobs)
  return ans
  
