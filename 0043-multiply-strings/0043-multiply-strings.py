class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        ans = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i, n1 in enumerate(num1):
            for j, n2 in enumerate(num2):
                temp = int(n1) * int(n2)
                ans[i+j] += temp % 10
                c = 0
                if ans[i+j] > 9:
                    c = ans[i+j] // 10
                    ans[i+j] = ans[i+j] % 10
                ans[i+j+1] += (temp//10 + c)
        ret = ""
        zero = True
        # print(ans)
        for x in ans[::-1]:
            if zero and x == 0:
                continue
            zero = False
            ret += str(x)
        return ret