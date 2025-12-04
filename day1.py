import common.fileutils as futils
import functools as fn


los = futils.getlos("day1.txt")

tlos = ["3 4\n",
	"4 3\n",
	"2 5\n",
	"1 3\n",
	"3 9\n",
	"3 3"]
	
tans = 11


def comparelists(text_list):
	left = list()
	right = list()
	
	for line in text_list:
		num1, num2 = map(int, line.strip().split())
		left.append(num1)
		right.append(num2)
	
	left.sort()
	right.sort()
	
	total = 0
	for i in range(0,len(left)):
		total += abs(left[i] - right[i])
	
	
	return total


print(comparelists(los))
#print(numbersfromlist(los))
#testnumbersfromlist(tlos2)




