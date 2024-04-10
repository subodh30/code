class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        s=[]
        while dirs:
            x = dirs.pop(0)
            if x == "" or x == ".":
                continue
            elif x == "..":
                if s:
                    s.pop()
            else:
                s.append(x)
        ans = ""
        for d in s:
            ans += "/" + d
        if ans == "":
            return "/"
        return ans