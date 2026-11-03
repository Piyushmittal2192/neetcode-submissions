class Solution:
    def isValid(self, s: str) -> bool:
        
        # every open brackt is closed by the same type
        # [] -> valid, ][ -> non 
        
        #

        hashmap = {'(': ')', '[': ']', '{':'}'} 

# ][]

# [{(]q])}]

# 1. stack, enter each character in the stack
# if the stack is 
# ]

        stack = []

        for char in s:
            if char in hashmap.keys():
                stack.append(char)

            
            # check if the stack is not empty, compare the stack last elemtn with the current char if the the new char is closed form of the last element of the stack then the pop the open bracket
            # enter the element in the stack


            else:
                if stack and hashmap[stack[-1]] == char:
                    stack.pop()
                else:
                    return False 

        
        return False if stack else True
