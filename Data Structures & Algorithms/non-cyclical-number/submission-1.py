class Solution:
    def isHappy(self, n: int) -> bool:
        curr = str(n)
        seen = set()

        while curr not in seen:
            seen.add(curr)
            total = 0
            for i in curr:
                i = int(i)
                total += i ** 2
            if total == 1: return True
            curr = str(total)

        return False