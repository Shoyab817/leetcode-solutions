class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""

        start, max_len = 0, 1

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1
        

        for i in range(len(s)):
            l, r = expand(i, i)
            if r - l + 1 > max_len:
                start, max_len = l, r - l + 1

            l, r = expand(i, i + 1)
            if r - l + 1 > max_len:
                start, max_len = l, r - l + 1

        return s[start : start + max_len]