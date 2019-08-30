class Solution():

	def appendInArray(self, array, num):

		if not array:
			array.append(num)
			return num

		left = 0 
		right = len(array)-1

		if num[1]<=array[left][1]:
			array.insert(0,num)
			return
		if num[1]>=array[right][1]:
			array.append(num)
			return

		while left<=right:
			mid = (left+right)/2 
			
			if left==right or array[mid][1] == num[1]:
				if num[1]>array[mid][1]:
					array.insert(mid+1,num)
				else:
					array.insert(mid,num)
				return
			if num[1]>array[mid][1]:
				left = mid+1
			else:
				right = mid

	def hotelBookingPossible(self, arrivalDate, departureDate, K):
		combinedDate = []

		for i in range(len(arrivalDate)):
			combinedDate.append([arrivalDate[i], departureDate[i]])

		combinedDate.sort()

		# print combinedDate

		movingWindow = []

		for elem in combinedDate:

			if elem[0] == elem[1]:
				continue

			while movingWindow and movingWindow[0][1]<=elem[0]:
				movingWindow.pop(0)

			self.appendInArray(movingWindow, elem)

			# print len(movingWindow)

			if len(movingWindow)>K:
				return False

		return True

s = Solution()
print s.hotelBookingPossible([ 17, 0, 45, 11, 16, 43, 15, 42, 2, 41, 0, 27, 37, 25, 17, 42, 24, 23, 11, 4, 29, 39, 6, 10, 42, 16, 17, 39, 1 ],[ 25, 24, 52, 51, 26, 46, 25, 45, 9, 51, 49, 48, 51, 66, 65, 57, 69, 43, 50, 9, 32, 55, 10, 58, 62, 46, 19, 87, 12 ],16)				
# s.appendInArray(a,[27,48])
