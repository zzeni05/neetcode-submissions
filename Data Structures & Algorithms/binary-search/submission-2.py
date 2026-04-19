class Solution:
    def search(self, nums: List[int], target: int) -> int:
        middle = len(nums) / 2
        middle = int(middle)
        searchLeft = True

        if nums[middle] > target:
            searchLeft = True
        else:
            searchLeft = False

        if searchLeft:
            for i in range(0, middle):
                if nums[i] == target:
                    return i
        else:
            for i in range(middle, len(nums)):
                if nums[i] == target:
                    return i
        return -1
        