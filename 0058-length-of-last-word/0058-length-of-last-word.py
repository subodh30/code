class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ss = s.split(" ")
        for i in ss[::-1]:
            if len(i) != 0:
                return len(i)