class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        d = {}
        for email in emails:
            local, domain = email.split("@")
            i=0
            ll = ""
            while i < len(local):
                if local[i] == "+":
                    break
                if local[i] != ".":
                    ll+=local[i]
                i+=1
            
            key = (ll, domain)
            if d.get(key, None) == None:
                d[key] = 0
            d[key] += 1
            
        # print(d)
        return len(d)