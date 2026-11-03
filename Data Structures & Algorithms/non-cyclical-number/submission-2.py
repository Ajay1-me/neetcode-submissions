class Solution:
    def isHappy(self, n: int) -> bool:
        # # Using the String function
        # curr = str(n)
        # seen = set()

        # while curr not in seen:
        #     seen.add(curr)
        #     total = 0
        #     for i in curr:
        #         i = int(i)
        #         total += i * i
        #     if total == 1: return True
        #     curr = str(total)

        # return False

        seen = set()

        while n not in seen:
            seen.add(n)
            n = self.sumOfSquares(n)
            if n == 1:  return True
        return False

    def sumOfSquares(self, n: int) -> int:
        total = 0

        while n:
            digit = n % 10
            digit = digit * digit
            total += digit
            n = n // 10   
        return total 




