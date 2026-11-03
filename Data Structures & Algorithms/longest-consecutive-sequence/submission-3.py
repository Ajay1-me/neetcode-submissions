class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums) # Removes all the duplicate when you put them in a set
        
        longest = 0

        for number in numbers:
            if number - 1 not in numbers:
                current = number
                current_length = 1

                while current + 1 in numbers:
                    current += 1
                    current_length += 1
                
                longest = max(longest, current_length)


        return longest        