"""
Problem 1 (linear version)

Given a sorted Python list of distinct integers, use linear search to return all
indices i such that the elements at index i equals i.

Input type: Python list
Output type: Python list
"""
def linearSearchValueIndexEqual(plist):
    if len(plist) == 0:
        return plist
    output_list = []
    for i in range(len(plist)):
        if plist[i] == i:
            output_list.append(plist[i])
    return output_list

"""
Problem 1 (binary version)

Given a sorted Python list of distinct integers, use binary search to return all
indices i such that the elements at index i equals i.

Input type: Python list
Output type: Python list
"""


def binarySearchValueIndexEqual(plist):
    return binarySearchValueIndexEqualHelper(plist,0,len(plist) - 1,[])

def binarySearchValueIndexEqualHelper(plist,left,right,output_list):
    if right < left:
        return output_list
    else:
        middle_index = (right - left) // 2 + left
    if plist[middle_index] == middle_index:
        output_list.append(plist[middle_index])
        return binarySearchValueIndexEqualHelper(plist,middle_index+1,right,output_list) and binarySearchValueIndexEqualHelper(plist,left,middle_index - 1,output_list)
    elif plist[middle_index] > middle_index:
        return binarySearchValueIndexEqualHelper(plist,left,middle_index - 1,output_list)
    else:
        return binarySearchValueIndexEqualHelper(plist,middle_index + 1,right,output_list)

"""
Problem 2 (linear version)

Let plist be a Python list of distinct integers sorted in ascending order.
Suppose plist is shifted to the right k times (0 <= k < len(plist)).
Write a function that finds the k using linear search.

Input type: Python list
Output type: integer
"""
def linearSearchShift(plist):
    if plist == []:
        return 0
    for i in range(len(plist)):
        if plist[i] == min(plist):
            break
    return i

"""
Problem 2 (binary version)

Let plist be a Python list of distinct integers sorted in ascending order.
Suppose plist is shifted to the right k times (0 <= k < len(plist)).
Write a function that finds the k using binary search.

Input type: Python list
Output type: integer
"""
def binarySearchShift(plist):
    if plist == []:
        return 0
    return binarySearchShiftHelper(plist,list(range(len(plist))))

def binarySearchShiftHelper(plist,index_list):
        middle_index = (len(plist) - 1) // 2
        if len(plist) == 1:
            return index_list[middle_index]
        if plist[middle_index] > plist[len(plist)-1]:
            return binarySearchShiftHelper(plist[middle_index + 1:],index_list[middle_index+1:])
        else:
            return binarySearchShiftHelper(plist[:middle_index+1],index_list[:middle_index+1])






def foo(plist):
    if len(plist) <= 1:
        return plist
    return [min(plist)] + foo(plist[1:])

#plist = [9,4,12,11]
#print(foo(plist))


def binarySearch(plist, item):
    left = 0
    right = len(plist) - 1
    count = 0

    while count < 2:
        mid = (right - left) // 2 + left
        if item == plist[mid]:
            return True
        elif item < plist[mid]:
            right = mid - 1
        else:
            left = mid + 1
        count += 1

    return plist[left],plist[right],count



#jplist = [2,5,8,10,15,25,30,74,100,101,201]
#print(binarySearch(plist,74))



def search(plist, n):
    result = []
    for s in plist:
        if len(s) == n:
            result.append(s)
    return result

#plist = ["apple", "pear", "orange", "berry", "melon", "pineapple", "bean"]
#n = 4
#print(search(plist,n))

def selectionSort(plist):
    count = 0
    for i in range(len(plist)-1, 6, -1):
        count += 1
        idx_of_max = 0
        for j in range(1, i+1):
            if plist[j] > plist[idx_of_max]:
                idx_of_max = j
        plist[i], plist[idx_of_max] = plist[idx_of_max], plist[i]
    return plist,count

#plist = [50, 40, 90, 3, 8, 10, 70, 5, 2, 11]
#print(selectionSort(plist))

class Coffee:
    def __init__(self, t, p):
        self.type = t
        self.price = p


