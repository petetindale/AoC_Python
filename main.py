import functools as fn
from common.data_handler import datahandler
from scripts import runner

cyear = 2025 #current year
cday = 8 #current day
cpart = 1 #part 1 or 2
ctest = False
#ctest = True

dh = datahandler(cyear, cday)

print("============================")
print("Advent of Code")
print("============================")
print(f"Year: {cyear} Day: {cday} Part: {cpart}")
print("============================")
if ctest :
  print("::: TEST RUN ::: ")

ans = runner.run(cyear, cday, cpart, dh.data if not ctest else dh.testdata)

if not ctest :
  print(f"Answer = {ans}")
else :
  print(f"Expected = {dh.testans(cpart)} - Actual = {ans}")
  print("PASS" if dh.testans(cpart) == ans else "FAIL")

