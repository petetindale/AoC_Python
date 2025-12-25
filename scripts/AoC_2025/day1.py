def spinwheel(input_data:list):
  pos = 50
  count = 0
  for x in input_data:
    dir = x[0]
    spin = int(x[1:])
    spin = spin % 100 
    
    if x[0] == "L":
      pos = pos - spin
    else :
      pos = pos + spin
    
    if pos % 100 == 0:
      count = count + 1
    elif pos < 0:
      pos = 100 + pos
    elif pos > 99:
      pos = pos - 100
      
    print(f"{x}-{spin}-{pos}")
      
  return count
  
def spinwheel2(input_data:list):
  pos = 50
  count = 0
  for x in input_data:
    dir = x[0]
    spin = int(x[1:])
    count = count + spin // 100
    spin = spin % 100 
    
    if x[0] == "L":
      pos = pos - spin
    else :
      pos = pos + spin
    
    if pos % 100 == 0 and spin != 0:
      count = count + 1
      pos = 0
      
    elif pos < 0:
      if pos + spin != 0:
        count = count +1 
      pos = 100 + pos
      
    elif pos > 99:
      pos = pos - 100
      count = count + 1
      
    #print(f"{x}-S:{spin}-P:{pos}--C:{count}")
      
  return count

def run(part:int, input_data:list):
  print(f"Day 1 - Part {part}")
  ans = 0
  if part == 1 :
    ans = spinwheel(input_data)
  else :
    ans = spinwheel2(input_data)
  return ans
  
