import math
import random

# ------------------------------------------------------------- #
num_list = [6, 3, 4, 1, 2, 3, 5, 7, 13]
# Selection Sorting
def selection_sort(list):

    for i in range(len(list)):
        
        for j in range(i, len(list)):

            if list[i] > list[j]:
                temp = list[j]
                list[j] = list[i]
                list[i] = temp


# ------------------------------------------------------------- #
# Bubble Sorting
def bubble_sort(list):

    for e in range(len(list) - 1, 0, -1):
        
        for i in range(e):
            if list[i] > list[i+1]:
                list[i] = list[i] ^ list[i+1]
                list[i+1] = list[i] ^ list[i+1]
                list[i] = list[i] ^ list[i+1]

    print(list)


# ------------------------------------------------------------- #
# Insertion Sorting
def insertion_sort(list):
    for e in range(1, len(list)):
        for i in range(e-1, -1, -1):
            if list[i+1] < list[i]:
                list[i+1] = list[i+1] ^ list[i]
                list[i] = list[i+1] ^ list[i]
                list[i+1] = list[i+1] ^ list[i]

    print(list)



# ------------------------------------------------------------- #
# Merge Sorting
def merge_sort(list, left_index, right_index):
    if left_index == right_index:
        return

    midpoint = left_index + ((right_index - left_index) >> 1)
    merge_sort(list, left_index, midpoint)
    merge_sort(list, midpoint + 1, right_index)
    merge(list, left_index, midpoint, right_index)


def merge(list, left, mid, right):
    temp = [0] * (right - left + 1)
    i = 0
    p1 = left
    p2 = mid + 1

    while (p1 <= mid and p2 <= right):
        if list[p1] < list[p2]:
            temp[i] = list[p1]

            p1 = p1 + 1
            i = i + 1
        else:
            temp[i] = list[p2]
            p2 = p2 + 1
            i = i + 1

    while (p1 <= mid):
        temp[i] = list[p1]
        i = i + 1
        p1 = p1 + 1

    while (p2 <= right):
        temp[i] = list[p2]
        i = i + 1
        p2 = p2 + 1

    for i in range(len(temp)):
        list[left+i] = temp[i]
    
# print(num_list)
# merge_sort(num_list, 0, len(num_list)-1)
# print(num_list)

# ------------------------------------------------------------- #
# Quick Sort
def quick_sort(list, left_index, right_index):
    if left_index < right_index:
        swap(list, random.randint(left_index,right_index), right_index)
        p = partition(list, left_index, right_index)
        quick_sort(list, left_index, p[0] - 1)
        quick_sort(list, p[1] + 1, right_index)

def partition(list, left, right):
    less = left - 1
    more = right
    
    while left < more:
        if list[left] < list[right]:
            less = less + 1
            swap(list, less, left)
            left = left + 1
        elif list[left] > list[right]:
            more = more - 1
            swap(list, more, left)
        else:
            left = left + 1

    swap(list, more, right)
    return [less+1, more]

def swap(list, index_one, index_two):
    temp = list[index_one]
    list[index_one] = list[index_two]
    list[index_two] = temp


# print(num_list)
# quick_sort(num_list, 0, len(num_list)-1)
# print(num_list)


# ------------------------------------------------------------- #
# Heap Sort
def heap_sort(list):
    if list == None or len(list) < 2:
        return
    
    # Create a max heap
    for i in range(len(list)):
        heap_insert(list, i)

    heap_size = len(list) - 1
    swap(list, 0, heap_size)
    while heap_size > 0:
        heapify(list, 0, heap_size)
        heap_size = heap_size - 1
        swap(list, 0, heap_size)


def heap_insert(list, index):
    while list[index] > list[int((index - 1)/2)]:
        swap(list, index, int((index - 1)/2))
        index = int((index - 1)/2)


def heapify(list, index, heap_size):
    left = index * 2 + 1
    while left < heap_size:

        # Determine whether left or tighr child value higher
        largest = (left, left+1)[list[left+1] > list[left] and left + 1 < heap_size]

        # Determine whether the value of parrent or the highest child value, higher
        largest = (index, largest)[list[largest] > list[index]]

        # Mean parent has higher value, stop heapify process
        if largest == index: break

        swap(list, largest, index)
        index = largest

        # Go to lower level of heap
        left = index * 2 + 1


# print(num_list)
# heap_sort(num_list)
# print(num_list)


# ------------------------------------------------------------- #
# non-comparative sort #
# ------------------------------------------------------------- #

num_list2 = [100, 123, 72, 6, 3445, 455, 3, 27]

# Radix Sort
def radix_sort(list):
    if list == None or len(list) < 2:
        return

    radix_operation(list, 0, len(list) - 1, get_maxbits_from_list(list))

def get_digit(element, digit):
    return int(element / math.pow(10, digit - 1) % 10)

def get_maxbits_from_list(list):
    max_value = - 0.000001
    for i in range(len(list)):
        max_value = max(max_value, list[i])
    max_digit_num = 0
    while(max_value != 0):
        max_digit_num += 1
        max_value = int(max_value/10)
    return max_digit_num

def radix_operation(list, left_index, right_index, max_digit):
    RADIX = 10
    bucket = [0] * (right_index - left_index + 1)
    j = 0
    for d in range(1, max_digit+1):

        # Container for digit count
        count = [0] * RADIX
        
        # Get digit count
        for i in range(left_index, right_index+1):
            j = get_digit(list[i], d)
            count[j] += 1
        
        # Get cumulative count
        for i in range(1, RADIX):
            count[i] = count[i] + count[i-1]

        # Fill number into bucket
        for i in range(right_index, left_index-1, -1):
            j = get_digit(list[i], d)
            bucket[count[j]-1] = list[i]
            count[j] -= 1

        
        for i, j in zip(range(left_index, right_index+1), range(0, len(bucket))):
            list[i] = bucket[j]

    print(list)
            

print(num_list2)
radix_sort(num_list2)