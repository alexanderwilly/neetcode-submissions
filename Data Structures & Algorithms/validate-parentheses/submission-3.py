class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')', '{':'}', '[':']'}
        stack = []

        for i in range(len(s)):
            if len(stack) > 0:
                # check top stack
                if brackets.get(stack[-1]) == s[i]:
                    stack.pop()
                else:
                    stack.append(s[i])        
            else:
                stack.append(s[i])
        
        

        return len(stack) == 0
        