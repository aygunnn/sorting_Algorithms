
import random


def buble_sort(array):
    
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j] , array[j+1] = array[j+1] , array[j]


arr = [12,67,23,56,12,98,34,97]
arr2 = random.sample(range(0,1000),10)

buble_sort(arr)
print(arr)


