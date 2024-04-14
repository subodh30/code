class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def get(num):
            num -= 1
            row = len(board) -1 - (num  // len(board))
            if len(board) % 2 == 0:
                if row % 2 == 1:
                    return row, num % len(board)
                else:
                    return row, len(board) -1 - (num % len(board))
            else:
                if row % 2 == 0:
                    return row, num % len(board)
                else:
                    return row, len(board) -1 - (num % len(board))
        # for i in range(1, len(board)**2 + 1):
        #     print("{}, {}".format(i, get(i)))
        def bfs():
            q = [(1,0)]
            vis = set()
            vis.add(1)
            target = len(board) ** 2
            while q:
                # print(q)
                x, ans = q.pop(0)
                for i in range(1,7):
                    num = x+i
                    if num > target:
                        continue
                    r,c = get(num)
                    val = board[r][c]
                    # print("{}, {}, {}".format(num, (r,c), val))
                    if val != -1:
                        if val == target:
                            return ans+1
                        if val not in vis:
                            vis.add(val)
                            q.append((val, ans+1))
                    else:
                        if num == target:
                            return ans + 1
                        if num not in vis:
                            vis.add(num)
                            q.append((num, ans+1))
                    
            return -1
        
        return bfs()
                
                
            
            
            
            