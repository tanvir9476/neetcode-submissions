class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        sign = True if x < 0 else False
        if sign:
            x = -1 * x
        int_min, int_max = -2**31, 2**31 - 1

        digits = ""

        while x:
            digit = x%10
            digits += str(digit)
            x //= 10

        x_rev = -1*int(digits) if sign else int(digits)
        # print(x_rev)

        if x_rev < int_min or x_rev > int_max:
            return 0
        else:
            return x_rev

