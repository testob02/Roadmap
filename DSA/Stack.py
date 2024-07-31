from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0
    
    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)
    
    def reverse_string(self, data):
        for char in data:
            self.push(char)

        reversed_string = ''
        while self.is_empty() is False:
            reversed_string += self.pop()

        return reversed_string

    def match(self, ch1, ch2):
        match_dict = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        return match_dict[ch2] == ch1 

    def check_parantheses(self, data):
        for char in  data:
            if char == '(' or char == '[' or char == '{':
                self.push(char)

            if char == ')' or char == ']' or char == '}':
                if self.is_empty():
                    return False
                if self.match(self.pop(),char) is False:
                    return False           
        
        return True
                
myStack = Stack()

print(myStack.reverse_string("We will conquer COVID-19"))
print(myStack.reverse_string("I am the king"))
print(myStack.reverse_string("I am a boy!!"))
print(myStack.check_parantheses("({a+b})"))
print(myStack.check_parantheses("))((a+b}{"))
print(myStack.check_parantheses("((a+b))"))
print(myStack.check_parantheses("))"))
print(myStack.check_parantheses("[a+b]*(x+2y)*{gg+kk}"))
print(myStack.check_parantheses("(abdulhakeem is funny,no{but faizullah)})"))
