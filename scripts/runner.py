from . import AoC_2025

def _operator(year:int): 
  rn = {
    "year2025day1": AoC_2025.day1.run,
    "year2025day2": AoC_2025.day2.run,
    "year2025day3": AoC_2025.day3.run,
    "year2025day4": AoC_2025.day4.run,
    "year2025day5": AoC_2025.day5.run,
    "year2025day6": AoC_2025.day6.run,
    "year2025day7": AoC_2025.day7.run,
    "year2025day8": AoC_2025.day8.run 
  }
  return rn
  
def run(year:int, day:int, part:int, input_data:list):
  op = _operator(year)
  return op[f"year{year}day{day}"](part, input_data)


