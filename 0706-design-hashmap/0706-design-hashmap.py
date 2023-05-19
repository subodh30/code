class Node:
    def __init__(self, key, val, next):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.h=[None]*1001

    def put(self, key: int, value: int) -> None:
        i = key%1001
        head = self.h[i]
        while(head!=None):
            if head.key==key:
                head.val = value
                break
            head=head.next
        if head == None:
            self.h[i] = Node(key, value, self.h[i])
        

    def get(self, key: int) -> int:
        i = key%1001
        head=self.h[i]
        while(head!=None):
            if head.key==key:
                return head.val
            head=head.next
        return -1
        

    def remove(self, key: int) -> None:
        i=key%1001
        
        head=self.h[i]
        prev = None
        if head==None: return
        if(head.key == key):
            self.h[i] = head.next
            return
        while(head!=None):
            if key == head.key:
                prev.next = head.next
                break
            prev = head
            head = head.next
                
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)