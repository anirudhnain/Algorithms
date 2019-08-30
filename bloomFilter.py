def bloomFilters(x):
	allOne = True
	for i in range(1,5):
		index = (i*x + x**(i-1))%m
		if arr[index] != 1:
			allOne = False
		arr[index] = 1
		# print ("index:",index)
	print (arr)
	return allOne
	# 	arr[index] = 1

i = 2018
m = 32
arr = [0]*m
while True:
	if bloomFilters(i):
		print ("False Positive i:", i)
		break
	i+=1