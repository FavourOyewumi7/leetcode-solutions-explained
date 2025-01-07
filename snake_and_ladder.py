"""
    algorithm  - BFS
    thought process:
    1. create a cells array conataing the position of each cell in the board in a snake and ladder game
    2. create a distance array to store the distance of each cell from the start cell
    3. create a queue to store the cells to be processed
    4. while the queue is not empty, pop the first cell from the queue and process it
    5. for each cell, check if the cell is a snake or ladder, if it is, 
    then the destination cell is the cell that the snake or ladder points to, if it is not, then the destination cell is the next cell
    6. if the destination cell is not visited, then mark it as visited and add it to the queue
    7. if the destination cell is the last cell, then return the distance of the destination cell
    """
class Solution:
        def snakesAndLadders(self, board):
            
            n = len(board)
            cells = [None] *(n*n+1)
            cols = list(range(0,n))
            l = 1
            for row in range(n-1, -1, -1):
                for col in cols:
                    cells[l] = (row,col)
                    l += 1
                cols.reverse()
            distance = [-1] * (n*n+1)
            distance[1] = 0
            queue = deque([1])

            while queue:
                curr = queue.popleft()
                for next in range(curr + 1,min(curr+6, n*n)+1):
                    r, c = cells[next]
                    dest = board[r][c] if board[r][c] != -1 else next
                    if distance[dest] == -1:
                        distance[dest] = distance[curr] + 1
                        queue.append(dest)
            return distance[n*n]
                
