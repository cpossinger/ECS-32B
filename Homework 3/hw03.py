"""
Queue class used for Problem 1
"""
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

"""
Node and UnorderedList classes used for Problem 2-5
"""
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
1. Stack2 class
Implement stack data structure using queue
"""
class Stack2:
    def __init__(self):
        self.queue = Queue()

    def isEmpty(self):
        return self.queue.isEmpty()

    def push(self, item):
        self.queue.enqueue(item)
    def pop(self):
        return self.queue.items.pop(0)
    def peek(self):
        return self.queue.items[0]
    def size(self):
        return self.queue.size()

"""
2. transform(lst)
Transform an unordered list into a Python list
Input: an (possibly empty) unordered list
Output: a Python list
"""
def transform(lst):
    cur = lst.head
    output_lst = list()
    if lst.isEmpty():
        return []
    while cur.getNext() != None:
        output_lst.append(cur.getData())
        cur = cur.getNext()
    output_lst.append(cur.getData())
    return output_lst




# lst = UnorderedList()
# lst.add(3)
# lst.add(2)
# lst.add(1)
# print(transform(lst))

"""
3. concatenate(lst1, lst2)
Concatenate two unordered lists
Input: two (possibly empty) unordered list
Output: an unordered list
"""
def concatenate(lst1, lst2):
    cur = lst1.head
    if lst1.isEmpty() and lst2.isEmpty():
        return lst1
    if lst1.isEmpty():
        lst1.head = lst2.head
        return lst1
    while not cur.getNext() == None:
        cur = cur.getNext()
    cur.setNext(lst2.head)
    return lst1


# lst1 = UnorderedList()
# lst1.add(3)
# lst1.add(2)
# lst1.add(1)
#
# lst2 = UnorderedList()
# lst2.add(6)
# lst2.add(5)
# lst2.add(4)
#
# lst_solution = concatenate(lst1,lst2)
# cur = lst_solution.head
# while cur.getNext() != None:
#     print(cur.getData())
#     cur = cur.getNext()
# print(cur.getData())
# print(lst_solution.length())
"""
    4. removeNodesFromBeginning(lst, n)
    Remove the first n nodes from an unordered list
    Input:
        lst -- an (possibly empty) unordered list
        n -- a non-negative integer
    Output: an unordred list
    """
def removeNodesFromBeginning(lst, n):
    cur = lst.head
    if lst.isEmpty():
        return lst
    for i in range(n):
       cur = cur.getNext()
    lst.head = cur
    return lst

# lst = UnorderedList()
# lst.add(5)
# lst.add(4)
# lst.add(3)
# lst.add(2)
# lst.add(1)

# lst_solution = removeNodesFromBeginning(lst,3)
# cur = lst_solution.head
# while cur.getNext() != None:
#     print(cur.getData())
#     cur = cur.getNext()
# print(cur.getData())
# print(lst_solution.length())

"""
    5. removeNodes(lst, i, n)
    Starting from the ith node, remove the next n nodes
    (not including the ith node itself).
    Assume i + n <= lst.length(), i >= 0, n >= 0.
    Input:
        lst -- an unrdered list
        i -- a non-negative integer
        n -- a non-negative integer
    Output: an unordred list
"""
def removeNodes(lst, i, n):
    ith = lst.head
    nth = lst.head
    count_ith = 0
    count_nth = 0
    if lst.isEmpty():
        return lst
    if ith.getNext() == None and n > 0:
        return UnorderedList()
    while count_ith < i-1:
        ith = ith.getNext()
        count_ith += 1
    while count_nth < (i-1) + (n+1):
        nth = nth.getNext()
        count_nth += 1
    ith.setNext(nth)
    return lst


# lst = UnorderedList()
# lst.add(6)
# lst.add(5)
# lst.add(4)
# lst.add(3)
# lst.add(2)
# lst.add(1)
#
# lst_solution = removeNodes(lst,2,3)
# cur = lst_solution.head
# while cur.getNext() != None:
#     print(cur.getData())
#     cur = cur.getNext()
# print(cur.getData())
# print(lst_solution.length())






