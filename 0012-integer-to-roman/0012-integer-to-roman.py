class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1:'I', 4: 'IV', 9:'IX', 40:'XL', 90:'XC', 400: 'CD', 900: 'CM'}
        
        keys = sorted(d.keys(), reverse=True)
        ans = ""
        while num > 0:
            for k in keys:
                if num - k >= 0:
                    ans += d[k]
                    num -= k
                    break
        return ans
            