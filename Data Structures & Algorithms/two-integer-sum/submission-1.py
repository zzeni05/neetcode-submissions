class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        sum = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    output.append(i)
                    output.append(j)
                    return output
        return output
        