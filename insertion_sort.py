
"""
1 - hoose one element
2 - if this element is smaller than the left one, put the element on that index
3 - repeats this for sorting ends

"""
import random

def insertion_sort(array):
     
    for i in range(1, len(array)):

        element = array[i]

        j = i-1
        while j >= 0 and element < array[j] :
                array[j + 1] = array[j]
                j -= 1
        array[j + 1] = element

sample_array = random.sample(range(0,100),5)

insertion_sort(sample_array)
print(sample_array)