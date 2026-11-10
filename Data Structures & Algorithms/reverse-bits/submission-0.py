class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        digits = [int(digit) for digit in format(n, "032b")]
        expo = 0
        for i in digits:
            if i == 1:
                res += 2 ** expo
                expo += 1
            else:
                expo += 1
        return res

