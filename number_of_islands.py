"""
Thought process:

1. We need to traverse the grid and find the number of islands
2. we use a bfs to traverse the grid and find the number of islands
3. we use a queue to traverse the grid and find the number of islands
"""
class Solution:
    def numIslands(self, grid):
        count = 0
        m, n = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        
        def bfs(r,c):
            start = (r,c)
            queue.append(start)
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            while queue:
                pos = queue.popleft()
                for dire in directions:
                    x = pos[0]+dire[0]
                    y = pos[1]+dire[1]

                    if 0 <= x < m and 0 <=y < n and (x,y) not in visited and grid[x][y] == "1":
                        visited.add((x,y))
                        queue.append((x,y))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j)
                    count += 1
        return count
