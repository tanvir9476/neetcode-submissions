class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum([int(c) for c in bin(n)[2:]])