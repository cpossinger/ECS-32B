"""
1. Find the smallest number in a (non-empty) Python list
"""
def smallest(plist):
    if len(plist) == 1:
        return plist[0]
    if plist[0] < plist[1]:
        del plist[1]
    else:
        del plist[0]

    return smallest(plist)

#plist = [5]
#print(smallest(plist))



"""
2. Compute the sum of the first n items in the sequence 1, 4, 9, 16, ..., n^2 (n >= 1)
"""
def sumOfSequence(n):
    if n == 1:
        return 1
    return n**2 + sumOfSequence((n-1))


#print(sumOfSequence(3))

"""
3. Check if a (possibly empty) string is a palindrome
"""
def isPalindrome(s):
    if s == "":
        return True
    if s[0] != s[-1]:
        return False
    return isPalindrome(s[1:-1])

#print(isPalindrome("abcabc"))


"""
4. Number of different ways to get to the top of a ladder
"""
def ladder(n):
    if n == 0:
        return 1
    if n == 1:
        return ladder(0)
    return ladder(n-1) + ladder(n-2)

#print(ladder(10))























