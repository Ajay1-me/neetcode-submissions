class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums)):
            # Skip the duplicates after the sort
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) -1 

            while(left < right):
                total = nums[i] + nums[left] + nums[right]
                
                if(total < 0):
                    left += 1
                elif(total > 0):
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
            
        return result



        # # Brute force causes infinite loop with O(n^3)
        # result = []
        
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):

        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 triplet = sorted([nums[i], nums[j], nums[k]])

        #                 if triplet not in result:
        #                     result.append(triplet)

        # return result