def findbiggest(pos:dict, frompos:int, topos:int):
  for i in range(9,0,-1):
    if i in pos:
      possible = [x for x in pos[i] if frompos <= x <= topos]
      if possible:
        return min(possible)
  return -1

def overcharge(battery:str):
  positions = {
    int(d): [i for i, ch in enumerate(battery) if ch == d]
    for d in set(battery) if d.isdigit()
  }
  battlen = len(battery)
  overbatt = ""
  frompos = 0
  topos = battlen-12
  for t in range(12):
    pos = findbiggest(positions, frompos, topos)
    overbatt += str(battery[pos])
    frompos = pos + 1
    topos += 1
    
  return int(overbatt)
  
def maxjolt(battery:str):
  maxj = 0
  for i in range(len(battery)-1):
    #print(battery)
    jolt = int(str(battery[i]) + str(max(map(lambda x: x, battery[i+1:]))))
    if jolt > maxj:
      maxj = jolt
  return maxj

def processbatteries(batteries:list, overchargesw:bool):
  joltage = 0
  for battery in batteries :
    if overchargesw:
      joltage += overcharge(battery)
    else:
      joltage += maxjolt(battery)
  return joltage

#Need this in each day
def run(part:int, input_data:list):
  print(f"Day 3 - Part {part}")
  ans = 0
  if part == 1 :
    ans = processbatteries(input_data, False)
  else :
    ans = processbatteries(input_data, True)
  return ans
  
