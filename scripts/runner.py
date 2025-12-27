from . import AoC_2025

def _operator(year:int): 
  rn = {
    "year2025day1": AoC_2025.day1.run,
    "year2025day2": AoC_2025.day2.run,
    "year2025day3": AoC_2025.day3.run,
    "year2025day4": AoC_2025.day4.run    
  }
  return rn
  
def run(year:int, day:int, part:int, input_data:list):
  op = _operator(year)
  return op[f"year{year}day{day}"](part, input_data)


