class DetectSquares:

    def __init__(self):
        self.points = {}
        self.X = {}

    def add(self, point: List[int]) -> None:
        key = (point[0], point[1])
        if self.points.get(key, None) == None:
            self.points[key] = 0
        self.points[key]+=1
       
        
        if self.X.get(key[0], None) == None:
            self.X[key[0]] = set()
        self.X[key[0]].add(key)
        # print(self.points)
        

    def count(self, point: List[int]) -> int:
        tot = 0
        # print(point)
        if self.X.get(point[0], None) != None:
            # print(self.X[point[0]])
            for pt in self.X[point[0]]:
                diff = abs(pt[1] - point[1])
                # print(diff)
                if diff != 0:
                    topLeft = (pt[0]+diff, pt[1])
                    topRight = (point[0]+diff, point[1])
                    tot += self.points[pt] * self.points.get(topLeft, 0) * self.points.get(topRight, 0)
                    topLeft = (pt[0]-diff, pt[1])
                    # print(topLeft)
                    topRight = (point[0]-diff, point[1])
                    tot += self.points[pt] * self.points.get(topLeft, 0) * self.points.get(topRight, 0)
        return tot


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)