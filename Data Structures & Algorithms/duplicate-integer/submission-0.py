class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setList = set()
        for i, val in enumerate(nums):
            setList.add(val)
        if (len(setList) == len(nums)):
            return False
        else:
            return True
    

