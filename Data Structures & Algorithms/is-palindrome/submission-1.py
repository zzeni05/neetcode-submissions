class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(char for char in s if char.isalnum())
        leftPointer = 0
        rightPointer = len(s)-1
        
        for c in s:
            if s[leftPointer] != s[rightPointer] and rightPointer != leftPointer:
                return False
            else:
                leftPointer += 1
                rightPointer -= 1
        return True