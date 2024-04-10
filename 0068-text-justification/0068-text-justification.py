class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def getJustified(arr):
            if len(arr) == 1:
                space = maxWidth - len(arr[0])
                return arr[0] + " "*space
            length = 0
            for w in arr:
                length += len(w)
            curSpace = maxWidth - length 
            space = curSpace // (len(arr) - 1)
            extraSpace = curSpace % (len(arr) - 1)
            for i, word in enumerate(arr[:-1]):
                arr[i] = word + " "*space
                if extraSpace > 0:
                    arr[i] += " "
                    extraSpace -= 1
            return "".join(arr)
        ans = []
        temp, curLen =[], 0
        for word in words:
            if curLen + len(word) <= maxWidth:
                temp.append(word)
                curLen += len(word)
                curLen += 1
            else:
                ans.append(getJustified(temp))
                temp, curLen = [word], len(word) + 1
        if temp:
            last = temp[0]
            for x in temp[1:]:
                last += " "
                last += x
            space = maxWidth - len(last)
            last += " "*space
            ans.append(last)
        return ans
            