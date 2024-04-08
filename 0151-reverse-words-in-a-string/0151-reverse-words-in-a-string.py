import re
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = re.sub(r'\s+', " ", s)
        words = s.split(" ")
        return " ".join(words[::-1])
            