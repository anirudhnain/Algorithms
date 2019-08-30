import math
def formaula(n):
	x = 1/math.exp(n/1024)

	print ("Orlando P:", (x-1))
	print ("Original P:", (1-x**4)**4)

	print(4*math.log(1-x**4)/math.log(1-x))
	print(math.log((4*math.log(1-x**4)/(math.log(1-x))),2))

formaula(10)
# formaula(80)