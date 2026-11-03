class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()

        for item in nums:
            if item in hashSet:
                return True
            # if hashSet.contains(item)
            #     return true
            hashSet.add(item)
        
        return False