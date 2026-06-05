class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ''
        for s in strs:
            encodedStr += s + "\0"

        return encodedStr 

    def decode(self, s: str) -> List[str]:
        strs = []
        index = 0
        for i, c in enumerate(s):
            if c == "\0":
                strs.append(s[index:i])
                index = i+1
        
        return strs
        
        


