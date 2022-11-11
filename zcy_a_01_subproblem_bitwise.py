import math
from queue import PriorityQueue

# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# Bitwise Interview Question
# Determine which one number count is odd and the answer is 2
num_list2 = [2, 2, 3, 1, 5, 3, 1, 2, 5]

for i in range(len(num_list2)-1):
    num_list2[0] ^= num_list2[i+1]

# print(num_list2[0])

# ------------------------------------------------------------- #
# Determine which two number count is odd
# The answer is 7 and 5
num_list3 = [7, 7, 3, 1, 5, 3, 1, 7, 5, 5]

eor = 0
for i in range(len(num_list3)):
    eor ^= num_list3[i]

right_most_bit_value = eor & (~eor + 1)    # Get the right most bit(1)

eor2 = 0
for value in num_list3:
    if ((value & right_most_bit_value) == 0):
        eor2 ^= value

# print("Two integer which has odd count")
# print(eor2)

for value in num_list3:
    eor2 ^= value

# print(eor2)


# ------------------------------------------------------------- #
# ------------------------------------------------------------- #
# Subproblem
# Determine whether a number is exist
num_list4 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 6, 6, 7]

target = 7
t = math.floor(len(num_list4) / 2)

while True:
    if num_list4[t] == target:  break 
    t = (t + math.floor((len(num_list4) - t) / 2) ,t - math.ceil(t / 2))[num_list4[t] > target]


# ------------------------------------------------------------- #
# Determine left most number of >= target

target = 2
t = math.floor(len(num_list4) / 2)

while True:
    if num_list4[t] == target:
        if num_list4[t-1] == target:
            t = t - 1
        else:
            break
    else:
        t = (t + math.floor((len(num_list4) - t) / 2) ,t - math.ceil(t / 2))[num_list4[t] > target]

# ------------------------------------------------------------- #
# Determine the value[i] which is smaller than value[i-1] & value[i+1]
num_list5 = [4, 6, 5, 10, 9, 7, 6, 8, 4, 10, 7, 9, 11, 13, 8, 9]

t1 = math.ceil(len(num_list5) / 2 - 1)
t2 = t1

def search(t):
    if t == 0:
        if num_list5[t] < num_list5[t+1]: return t
    elif t == (len(num_list5) - 1):
        if num_list5[t] < num_list5[t-1]: return t
    else:
        if num_list5[t] < num_list5[t-1] and num_list5[t] < num_list5[t+1]: return t

while True:
    
    t = search(t1)
    if t != None : break
    t = search(t2)
    if t != None : break

    t1 = t1 + math.floor((len(num_list5) - t1) / 2)
    t2 = t2 - math.ceil(t2 / 2)
    
    
# print(t, num_list5[t])


# ------------------------------------------------------------- #
# Determine the max value in the array within certain range

def find_max(list, left_index, right_index):
    if left_index == right_index:
        return list[left_index]

    mid_point = left_index + ((right_index - left_index) >> 1)  #  >> 1 same as divide 2
    left_arr_max = find_max(list, left_index, mid_point)
    right_arr_max = find_max(list, mid_point + 1, right_index)    
    return max(left_arr_max, right_arr_max)


# print(num_list5[2:13]) 
# print(find_max(num_list5, 2, 12))

# ------------------------------------------------------------- #
# Can use merge sort algorithm to solve question below
# Determine the sum of the value in which the left side value smaller than i than while loop through n number
# [1, 3, 4, 2, 5] as input and the output is (1)+(1+3)+(1)+(1+3+4+2) = 16

def find_small_sum(list, left_ind, right_ind):
    if left_ind == right_ind:
        return 0

    midpoint = left_ind + ((right_ind - left_ind) >> 1)
    return find_small_sum(list, left_ind, midpoint) + \
           find_small_sum(list, midpoint+1, right_ind) + \
           merge(list, left_ind, midpoint, right_ind)

def merge(list, left_ind, midpoint, right_ind):
    temp = [0] * (right_ind - left_ind + 1)
    i = 0
    p1 = left_ind
    p2 = midpoint + 1
    small_sum = 0
    while p1 <= midpoint and p2 <= right_ind:
        if list[p1] < list[p2]:
            small_sum += list[p1] * (right_ind - p2 + 1)
            temp[i] = list[p1]
            p1 += 1
            i += 1
        else:
            temp[i] = list[p2]
            p2 += 1
            i += 1
    
    while p1 <= midpoint:
        temp[i] = list[p1]
        p1 += 1
        i += 1

    while p2 <= right_ind:
        temp[i] = list[p2]
        p2 += 1
        i += 1

    for i in range(len(temp)):
        list[left_ind+i] = temp[i]
    
    return small_sum


def swap(list, index_one, index_two):
    temp = list[index_two]
    list[index_two] = list[index_one]
    list[index_one] = temp

num_list = [1, 3, 4, 2, 5]
print(find_small_sum(num_list, 0, len(num_list)-1))





