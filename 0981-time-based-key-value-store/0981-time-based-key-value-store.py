class TimeMap:

    def __init__(self):
        self.d={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.d.get(key) == None:
            self.d[key] = [(timestamp, value)]
        else:
            self.d[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if self.d.get(key)==None:
            return ""
        arr = self.d[key]
        l, r = 0, len(arr)
        if timestamp < arr[0][0]:
            return ""
        while l < r:
            mid = (l+r)//2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] < timestamp:
                l = mid + 1
            else:
                r = mid
        return arr[l-1][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)