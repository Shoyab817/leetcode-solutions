class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        i = 0
        n = len(s)

        # Step 1: skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: determine sign
        sign = 1
        if i < n and s[i] in ('+', '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # Step 3: read digits
        result = 0
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result *= sign

        # Step 4: clamp to 32-bit signed integer range
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result