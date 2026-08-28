class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numMap = {}
        ans = []

        for i, n in enumerate(nums):
            diff = target - n
            if diff not in numMap.keys():
                numMap[n] = i


        for i, n in enumerate(nums):
            diff = target - n
            if diff in numMap.keys() and numMap[diff] != i:
                ans.append(numMap[diff])
                ans.append(i)
                return ans

        return ans

        

            


        