import heapq
from collections import defaultdict
from operator import itemgetter
"""
BinaryTreeNode class
"""
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data     # the data the node holds
        self.left = None    # a pointer to the left child
        self.right = None



"""
1. Reconstruct Binary Tree
"""
def reconstructBT(preorder, inorder):
    reconstructBTHelper.preorder_counter = 0
    return reconstructBTHelper(preorder,inorder,0,len(inorder) - 1)

def reconstructBTHelper(preorder,inorder,inorder_start,inorder_end):
    if inorder_start > inorder_end:
        return None
    root = BinaryTreeNode(preorder[reconstructBTHelper.preorder_counter])
    reconstructBTHelper.preorder_counter += 1
    if inorder_start == inorder_end:
        return root
    inorder_index = inorder.index(root.val)
    root.left = reconstructBTHelper(preorder,inorder,inorder_start,inorder_index - 1)
    root.right = reconstructBTHelper(preorder,inorder,inorder_index + 1,inorder_end)
    return root

"""
2. Convert Binary Search Tree
"""
def convertBSTtoGST(root):
    current = root
    stack = []
    node_values = []
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            node_values.append(current.val)
            current = current.right
        else:
            break
    return lst2Tree(root,node_values)

def lst2Tree(root,lst):
    GST_lst = []
    for i in range(len(lst)):
        GST_lst.append(sum(lst[i:]))
    lst.reverse()
    GST_lst.reverse()
    for i in range(len(lst)):
        node = searchBinaryTree(root,lst[i])
        node.val = GST_lst[i]
    return root


def searchBinaryTree(root,target):
    if not root:
        return None
    if root.val == target:
        return root
    if root.val < target:
        return searchBinaryTree(root.right,target)
    return searchBinaryTree(root.left,target)

"""
3. Top k Frequent Elements
"""
def kFrequent(nums, k):
    output_lst = []
    counter = {}
    counter_heap = []
    for i in nums:
        if i not in counter:
            counter[i] = -1
        else:
            counter[i] -= 1
    for key,value in counter.items():
        heapq.heappush(counter_heap,(value,key))
    print(counter_heap)
    counter_heap = heapq.nsmallest(len(nums),counter_heap,itemgetter(1))
    for i in heapq.nsmallest(k,counter_heap,itemgetter(0)):
        output_lst.append(i[1])
    return output_lst



"""
4. All paths from one vertex to another in DAG
"""
def allPaths(edges, source, destination):
    paths = []
    graph_dict = defaultdict(list)
    visited_dict = {}
    for i in edges:
        graph_dict[i[0]].append(i[1])
        if i[1] not in graph_dict:
            graph_dict[i[1]] = []
    print(graph_dict)
    for source_adj in graph_dict[source]:
        print("Source Adj: ",source_adj)
        if source_adj == destination:
            paths.append([source,source_adj])
        for j in graph_dict[source_adj]:
            print("j: ",j)
            if j == destination:
                paths.append([source,source_adj,j])
            for k in graph_dict[j]:
                print("k: ",k)
                if k == destination:
                    paths.append([source,source_adj,j,k])
                for l in graph_dict[k]:
                    print("l: ",l)
                    if l == destination:
                        paths.append([source,source_adj,j,k,l])

    return paths

