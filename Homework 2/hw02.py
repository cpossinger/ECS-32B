class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            print("pop() error: Stack is empty.")
            return None

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("peek() error: Stack is empty.")
            return None

    def size(self):
        return len(self.items)


class Solution:
    def postfixEval(self,expr):
        operand_str = ["+","-","*","/"]
        expr_stack = Stack()
        if len(expr) == 1:
            return float(expr[0])
        for i in expr:
            expr_stack.push(i)
            if expr_stack.peek() in operand_str:
                expr_stack.pop()
                num1 = expr_stack.pop()
                num2 = expr_stack.pop()
                new_expr = eval(num2+i+num1)
                expr_stack.push(str(new_expr))
        if expr_stack.size() == 1:
            return new_expr

    def validParentheses(self, s):
        par_stack = Stack()
        close_list = [")", "]", "}"]
        open_list = ["(","[","{"]
        balanced = True
        pop_count = 0
        if len(s) == 1 and s in close_list:
            return False
        if s == "":
            return True
        for i in s:
            if i in open_list:
                #print("push",i)
                par_stack.push(i)
            if i in close_list:
                if par_stack.isEmpty():
                    balanced = False
                else:
                    par_stack.pop()
        if par_stack.isEmpty() == True and balanced == True:
            return True
        else:
            return False




    def reverseString(self, s):
        reverse_str = list()
        str = Stack()
        if s == "":
            return ""
        for i in s:
            str.push(i)
        pop_count = str.size()
        while pop_count > 0:
            reverse_str.append(str.pop())
            pop_count -= 1
        return ''.join(reverse_str)









