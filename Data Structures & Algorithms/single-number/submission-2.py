class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashSet = set()

        for i in range(len(nums)):
            if nums[i] in hashSet:
                hashSet.remove(nums[i])
            else:
                hashSet.add(nums[i])
        return hashSet.pop()
