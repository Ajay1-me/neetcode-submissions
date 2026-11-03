class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, number in enumerate(nums):
            needed = target - number
            
            if needed in hashMap:
                return [hashMap[needed], i]
            
            hashMap[number] = i

        return [] 


        