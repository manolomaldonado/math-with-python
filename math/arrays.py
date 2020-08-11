import random
import time
a = [7,3,5,1,2,9,6,0,8,13,22,11,16]

def create_list(length) :
    return random.sample(range(length), length)


def pasada(a) : 
    for i in range(len(a)-1) :
        if a[i] > a[i+1] :
            c = a[i]
            a[i] = a[i+1]
            a[i+1] = c
    return a

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

def bubble_sort(array) :
    for i in range((len(array)//2)+1) :
        array = pasada(array)
    return array


a = create_list(1000)
b = create_list(10000)
start_time = time.time()
bubble_sort(a)
print(a)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
quick_sort(b, 0, len(b) - 1)
print(b)
print("--- %s seconds ---" % (time.time() - start_time))