class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        solution = []


        for i, v in enumerate(nums):
            numDict[v] = i
        
        for i, v in enumerate(nums):
            if target - v in numDict and numDict[target - v] != i:
                solution.append(i)
                solution.append(numDict[target - v])
                return solution



