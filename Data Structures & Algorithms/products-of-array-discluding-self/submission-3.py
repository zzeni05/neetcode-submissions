
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product = 1
        zero_count = 0

        for val in nums:
            if val == 0:
                zero_count += 1
            else:
                product *= val

        for val in nums:
            if zero_count > 1:
                result.append(0)
            elif zero_count == 1:
                if val == 0:
                    result.append(product)
                else:
                    result.append(0)
            else:
                result.append(product // val)
        
        return result

