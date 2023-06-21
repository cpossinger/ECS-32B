from hw02 import Solution     # or from hw02-framework import Solution



# set up
sol = Solution()

# test cases for postfixEval
def testPostfixEval():
    print("--- Testing postfixEval ---")

    test1 = ["2", "4", "7", "*", "-"]
    print("Test 1:", sol.postfixEval(test1) == -26)
    print("Function Value",sol.postfixEval(test1))

    # add as many test cases as you want

    print("--- Finished postfixEval ---\n")



# # test cases for validParentheses
def testValidParentheses():
    print("--- Testing validParentheses ---")

    test1 = "({})[]"
    print("Test 1:", sol.validParentheses(test1) == True)
    print("Function Value",sol.validParentheses(test1))
    # add as many test cases as you want

    print("--- Finished validParentheses---\n")



# # test cases for reverseString
def testReverseString():
    print("--- Testing reverseString ---")

    test1 = "abcde"
    print("Test 1:", sol.reverseString(test1) == "edcba")

    # add as many test cases as you want

    print("--- Finished reverseString---\n")



# Run the tests
testPostfixEval()
testValidParentheses()
testReverseString()
