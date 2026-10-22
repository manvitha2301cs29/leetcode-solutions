class Solution:
    def isPalindrome(self, s: str) -> bool:
        li = []
        for c in s.lower():
            if "a" <= c <= "z" or "0" <= c <= "9" :
                li.append(c)
        return li == li[::-1]
        