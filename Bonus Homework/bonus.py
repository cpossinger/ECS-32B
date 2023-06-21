class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, node):
        self.next = node



class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        newNode = Node(data)
        newNode.setNext(self.head)
        self.head = newNode

    def length(self):
        cur = self.head
        count = 0
        while cur:
            cur = cur.getNext()
            count += 1
        return count

    def isEmpty(self):
        return self.head == None

    def search(self, data):
        cur = self.head
        while cur:
            if cur.getData() == data:
                return True
            cur = cur.getNext()
        return False

    def remove(self, data):
        if self.head.getData() == data:
            self.head = self.head.getNext()
        else:
            cur = self.head
            while cur.getNext() and cur.getNext().getData() != data:
                cur = cur.getNext()
            if cur.getNext():
                cur.setNext(cur.getNext().getNext())



"""
1. Find the middle node of a linked list without calculating the length of the list
"""
def findMiddle(lst):
    if lst.isEmpty():
        return None
    else:
        return middleList(lst)

def middleList(lst):
    lst_data = []
    cur = lst.head
    while cur.getNext() != None:
        lst_data.append(cur.getData())
        cur = cur.getNext()
    lst_data.append(cur.getData())
    return findMiddleData(lst,lst_data)

def findMiddleData(lst,lst_data,next = None):
    if len(lst_data) == 3:
        print("length three")
        next = lst_data[2]
    if len(lst_data) == 1 or len(lst_data) == 2:
        if len(lst_data) == 2:
            return findMiddleNode(lst,lst_data[0],lst_data[1])
        else:
            return findMiddleNode(lst,lst_data[0],next)
    lst_data.pop(0)
    lst_data.pop()
    if next != None:
        return findMiddleData(lst,lst_data,next)
    else:
        return findMiddleData(lst,lst_data)


def findMiddleNode(lst,middle_data,middle_data_next = None):
    cur = lst.head
    while cur.getNext() != None:
        if cur.getData() == middle_data and cur.getNext().getData() == middle_data_next:
            break
        else:
            cur = cur.getNext()
    return cur




"""
2. Search for an item in a shifted Python list (distinct values)
"""
def search(plist, target):
    if plist == []:
        return -1
    input_lst = []
    for i in plist:
        input_lst.append((i,plist.index(i)))
    return bubbleSortShort(input_lst,target)



def bubbleSortShort(input_lst,target):
    if len(input_lst) == 1:
        return binarySearchShift(input_lst,target)
    for i in range(len(input_lst)-1,0,-1):
        exchanged = False
        for j in range(i):
            if input_lst[j][0] > input_lst[j+1][0]:
                input_lst[j],input_lst[j+1] = input_lst[j+1],input_lst[j]
                exchanged = True
        if not exchanged:
            return binarySearchShift(input_lst,target)

def binarySearchShift(input_lst,target):
    left = 0
    right = len(input_lst) - 1

    while left <= right:
        mid = (right - left) // 2 + left
        if target == input_lst[mid][0]:
            return input_lst[mid][1]
        elif target < input_lst[mid][0]:
            right = mid - 1
        else:
            left = mid + 1
    return -1






