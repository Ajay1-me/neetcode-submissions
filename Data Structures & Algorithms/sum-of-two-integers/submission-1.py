class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF      # 32 ones in binary
        max_positive = 0x7FFFFFFF  # Largest signed 32-bit integer

        a &= mask
        b &= mask

        while b:
            carry = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = carry

        # Convert a negative 32-bit result back to a Python negative integer
        return a if a <= max_positive else ~(a ^ mask)