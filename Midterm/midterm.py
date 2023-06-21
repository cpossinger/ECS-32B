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
Given two (possible empty) sorted linked lists (defined using the UnorderedList class above),
merge them and return it as a new sorted linked list (defined using the UnorderedList class).

The new list should be made by splicing together the nodes of the first two lists.

You may not transform each linked list into a Python list, merge them and return
a linked list from the resulting Python list.

Example 1
Input:
    l1: 5 -> 10 -> 11 -> 12 -> 15
    l2: 1 -> 2 -> 5 -> 14
Output:
    1 -> 2 -> 5 -> 5 -> 10 -> 11 -> 12 -> 14 -> 15

Example 2
Input:
    l1: 1 -> 2 -> 3
    l2: 4 -> 5 -> 6
Output:
    1 -> 2 -> 3 -> 4 -> 5 -> 6

Example 3
Input:
    l1: 1
    l2: 4 -> 5 -> 6
Output:
    1 -> 4 -> 5 -> 6
"""
def merge(l1, l2):
    return mergeHelper(l1,l2,UnorderedList())


def mergeHelper(l1,l2,sorted_list,biggest_data=-500):

    if l1.length() == 0 and l2.length() == 0:
        return sorted_list
    l1_cur = l1.head
    l2_cur = l2.head
    l1_len = l1.length()
    l2_len = l2.length()
    while l1_len > 0:
        if l1_cur.getData() > biggest_data:
            biggest_data = l1_cur.getData()
        l1_cur = l1_cur.getNext()
        l1_len -= 1
    while l2_len > 0:
        if l2_cur.getData() > biggest_data:
            biggest_data = l2_cur.getData()
        l2_cur = l2_cur.getNext()
        l2_len -= 1
    l1_cur = l1.head
    l2_cur = l2.head
    l1_len = l1.length()
    l2_len = l2.length()
    print("Biggest Data",biggest_data)
    if l1.search(biggest_data) is True:
        print("L1 True")
        while l1_len > 0:
            if l1_cur.getData() == biggest_data:
                print("Found L1")
                sorted_list.add(biggest_data)
                l1.remove(biggest_data)
            l1_cur = l1_cur.getNext()
            l1_len -= 1

    else:
        print("L2 True")
        while l2_len > 0:
            if l2_cur.getData() == biggest_data:
                print("Found L2")
                sorted_list.add(biggest_data)
                l2.remove(biggest_data)
            l2_cur = l2_cur.getNext()
            l2_len -= 1
    return mergeHelper(l1,l2,sorted_list)





# l1 = UnorderedList()
# l1.add(15)
# l1.add(10)
# l1.add(5)
#
# l2 = UnorderedList()
# l2.add(20)
# l2.add(3)
# l2.add(2)
# l2.add(-3)
#
#
# output = merge(l1,l2)
#
# cur = output.head
# while cur.getNext() != None:
#     print(cur.getData())
#     cur = cur.getNext()
# print(cur.getData())