"""
1. Tests whether the letters in a string can be permuted to form a palindrome.
"""
def canFormPalindrome(s):
    if s == "":
        return True
    odd_count = 0
    palendrome = True
    char_dict = {}
    even = False
    odd = False
    for i in s:
        if i not in char_dict:
            char_dict[i] = 1
        else:
            char_dict[i] += 1
    if len(s) % 2 == 0:
        even = True
    else:
        odd = True
    for i in char_dict.values():
        if odd == True:
            if (i % 2) == 1:
                odd_count += 1
            if odd_count != 1:
                palendrome = False
            else:
                palendrome = True
        if even == True:
            if (i % 2) != 0:
                palendrome = False
    return palendrome


"""
2. Determines if it is possible to write an anonymous letter using a book.
"""
def anonymousLetter(book, letter):
    if book == "" and letter == "":
        return True
    if letter == "":
        return True
    if book == "":
        return False
    book_dict = {}
    letter_dict = {}
    for i in book:
        if i not in book_dict:
            book_dict[i] = 1
        else:
            book_dict[i] += 1
    for i in letter:
        if i not in letter_dict:
            letter_dict[i] = 1
        else:
            letter_dict[i] += 1
    for i in letter_dict.keys():
        if i in book_dict.keys():
            if letter_dict[i] > book_dict[i]:
                return False
    return True


"""
3. Iterative preorder traversal of a binary tree
"""
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def preorder(root):
    output_lst = []
    if root == None:
        return output_lst
    output_lst.append(root.val)
    if root.left != None:
        cur_left = root.left
        output_lst.append(cur_left.val)
        while cur_left.left != None:
            cur_left = cur_left.left
            output_lst.append(cur_left.val)
        cur_left = root.left
        while cur_left.left != None:
            cur_left = cur_left.left
            if cur_left.right != None:
                output_lst.append(cur_left.right.val)

        if root.left.right != None:
            cur_left = root.left.right
            output_lst.append(cur_left.val)
        while cur_left.right != None:
            if cur_left.left != None:
                output_lst.append(cur_left.left.val)
            cur_left = cur_left.right
        if root.left.right != None:
            cur_left = root.left.right
        while cur_left.right != None:
            cur_left = cur_left.right
            output_lst.append(cur_left.val)

    if root.right != None:
        cur_right = root.right
        output_lst.append(cur_right.val)
        while cur_right.left != None:
            cur_right = cur_right.left
            output_lst.append(cur_right.val)
        cur_right = root.right
        while cur_right.left != None:
            cur_right = cur_right.left
            if cur_right.right != None:
                output_lst.append(cur_right.right.val)
        if root.right.right != None:
            cur_right = root.right.right
            output_lst.append(cur_right.val)
        while cur_right != None:
            if cur_right.left != None:
                output_lst.append(cur_right.left.val)
            if cur_right.right != None:
                cur_right = cur_right.right
            else:
                break
        if root.right.right != None:
            cur_right = root.right.right
        while cur_right.right != None:
            cur_right = cur_right.right
            output_lst.append(cur_right.val)
        if root.right.right is not None:
            cur_right = root.right.right
            if cur_right.left is not None:
                cur_right = cur_right.left
        while cur_right.left != None:
            cur_right = cur_right.left
            output_lst.append(cur_right.val)
        if root.right.right is not None:
            cur_right = root.right.right
            if cur_right.left is not None:
                cur_right = cur_right.left
        while cur_right.right != None:
            cur_right = cur_right.right
            output_lst.append(cur_right.val)

    return output_lst









