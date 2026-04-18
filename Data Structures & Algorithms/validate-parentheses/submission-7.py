class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMatching = {'{':'}', '[':']', '(': ')'}

        for c in s:
            if c == '{' or c == '[' or c == '(':
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop() 
                if bracketMatching[top] != c:
                    return False
        return len(stack) == 0
        return True