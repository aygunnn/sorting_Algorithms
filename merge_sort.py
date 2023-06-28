

def merge_sort(arr):
	
	if len(arr)>1:

		# array divisioned
		left = arr[:len(arr)//2]
		right = arr[len(arr)//2:]

		merge_sort(left)
		merge_sort(right)

		# Combine the arrays
		i = 0
		j = 0
		k = 0

		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				arr[k] = left[i]
				i+=1
				k+=1
			else :
				arr[k] = right[j]
				j+=1
				k+=1

		while i < len(left):
			arr[k] = left[i]
			i+=1
			k+=1
		
		while j < len(right):
			arr[k] = right[j]
			j+=1
			k+=1



array = [11,99,22,88,33,77,44,66,55]
merge_sort(array)
print(array)

