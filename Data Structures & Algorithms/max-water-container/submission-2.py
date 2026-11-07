class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # output = 0
        # for left in range(len(heights)):
        #     for right in range(left + 1, len(heights)):
        #         area = min(heights[left], heights[right]) * (right - left)
        #         output = max(output, area)
        # return output

        left, right = 0, len(heights) - 1
        output = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            output = max(output, area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return output