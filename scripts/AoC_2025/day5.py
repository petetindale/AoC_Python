import functools as fn

def findgoodfood(invrange:list, ingredients:list):
  count = 0
  for ind in ingredients :
    inrng = fn.reduce(lambda x, y: (1 if y[0] <= ind <= y[1] else 0) + x, invrange, 0)
    count += 1 if inrng > 0 else 0
  return count

def findallind(invrange:list) :
  cl = invrange
  cl.sort()
  
  distl = list()
  
  curmin = cl[0][0]
  curmax = cl[0][1]
  
  for i in cl:
    if i[0]==curmin and i[1]==curmax:
      #print("match")
      pass
    elif i[0] <= curmax :
      if i[1] > curmax :
        curmax = i[1]
      elif i[1] <= curmax :
        #print("within range")
        pass
    elif i[0] > curmax :
      distl.append([curmin,curmax])
      curmin = i[0]
      curmax = i[1]
      # print("next")
    else :
      print("how did we get here")
  
  distl.append([curmin,curmax]) #add last
  
  return distl

def findalliter(invrange:list):
  #this is really hacky but meh its low on memory. 
  cl = invrange
  prevlen = len(cl)
  currlen = 0
  while currlen != prevlen:
    prevlen = currlen
    cl=findallind(cl)
    currlen = len(cl)
  
  count = fn.reduce(lambda x,y:x+(y[1]-y[0]+1), cl, 0)
  
  return count

def processdb(invdb:list):
  invrange = list()
  ingredients = list()
  foundblank = False
  for i in invdb :
    if i == "" and not foundblank :
      foundblank = True
    elif not foundblank :
      invrange.append(list(map(lambda x: int(x), i.split("-"))))
    else :
      ingredients.append(int(i))
  
  return invrange, ingredients

#Need this in each day
def run(part:int, input_data:list):
  print(f"Day 5 - Part {part}")
  print(f"---First line length = {len(input_data[0])}---")
  
  invrange, ingredients = processdb(input_data)
  
  ans = 0
  if part == 1 :
    ans = findgoodfood(invrange, ingredients)
  else :
    ans = findalliter(invrange)
  return ans
  
