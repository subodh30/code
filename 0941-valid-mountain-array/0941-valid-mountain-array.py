class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        i=0
        asc=0
        dsc=0
        flag=True
        while i < len(arr)-1:
            if arr[i]==arr[i+1]:
                return False
            if flag:
                if arr[i] < arr[i+1]:
                    asc+=1
                else:
                    dsc+=1
                    flag=False
            else:
                if arr[i] > arr[i+1]:
                    dsc+=1
                else:
                    return False
            i+=1
        print(asc)
        print(dsc)
        return asc!=0 and dsc!=0
        