class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_count = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_count += 1
        
        if zero_count > 1: return [0] * len(nums)

        output = [0] * len(nums)
        for i, j in enumerate(nums):
            if zero_count: 
                output[i] = 0 
                if j != 0:
                    output[i] = 0
                else:
                    output[i] = prod
            else:
                output[i] = prod // j

        return output