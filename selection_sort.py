
"""
1 - accept this: first element is always smaller
2 - chooses the closest one of the first element and adds it in second index
3 - than chooses the closest one of the second element and adds it in the third index

"""



import random 
from datetime import datetime


def selection_sort(arr):

    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]

array = random.sample(range(0,100),5)
selection_sort(array)
print(array)

