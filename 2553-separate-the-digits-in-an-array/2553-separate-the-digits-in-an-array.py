class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            x = i
            temp =[]
            while x!=0:
                temp.append(x%10)
                x = x // 10
            ans.extend(temp[::-1])
        return ans
        