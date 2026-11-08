class Solution:
    def hammingWeight(self, n: int) -> int:
        #we keep on dividing by 2 and keep the count of cases where % is = 1
        count = 0
        while n != 0:
            # if n % 2 == 1:
            #     count += 1
            # n = n // 2
            n = n & (n - 1)
            count += 1
        return count
