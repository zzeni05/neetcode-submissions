class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        for i in range(len(nums)):
            leftProd = 1
            rightProd = 1

            for j in range(0, i):
                leftProd *= nums[j]

            for k in range(i + 1, len(nums)):
                rightProd *= nums[k]

            answer.append(leftProd * rightProd)

        return answer