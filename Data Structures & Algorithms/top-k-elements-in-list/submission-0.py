class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Start by maintaining the count of the numbers
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        
        arr = []
        for i, cnt in count.items():
            arr.append([cnt, i])
        arr.sort()

        result = []
        while len(result) < k:
            result.append(arr.pop()[1])
        return result
        # For debugging
        #return list(arr)

        