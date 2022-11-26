import sys 
# Approach only for Radial sensor
def isSafe(mat, visited, x, y):
    return (x >= 0 and x < len(mat) and y >= 0 and y < len(mat[0]) and mat[x][y] == 0 and (not visited[x][y]))
 
def findShortestPath(mat, visited, i, j, n, min_dist, dist):
    global covered
    if (covered == n):
        min_dist = min(dist, min_dist)
        print(visited)
        return min_dist
 
    # set (i, j) cell as visited
    if (i > 1 and j > 1 and i < 8 and j < 8):
        visited[i][j-1] = True
        visited[i][j-2] = True
        visited[i][j+1] = True
        visited[i][j+2] = True
        visited[i-1][j-1] = True
        visited[i-1][j+1] = True
        visited[i+1][j-1] = True
        visited[i+1][j+1] = True
        visited[i+1][j] = True
        visited[i+2][j] = True
        visited[i-1][j] = True
        visited[i-2][j] = True

     
    # go to the bottom cell
    if (isSafe(mat, visited, i + 1, j)):
        covered += 3
        min_dist = findShortestPath(
            mat, visited, i + 1, j, n, min_dist, dist + 1)
 
    # go to the right cell
    if (isSafe(mat, visited, i, j + 1)):
        covered += 3
        min_dist = findShortestPath(
            mat, visited, i, j + 1, n, min_dist, dist + 1)

    # go to the top cell
    if (isSafe(mat, visited, i - 1, j)):
        covered += 3
        min_dist = findShortestPath(
            mat, visited, i - 1, j, n, min_dist, dist + 1)
 
    # go to the left cell
    if (isSafe(mat, visited, i, j - 1)):
        covered += 3
        min_dist = findShortestPath(
            mat, visited, i, j - 1, n, min_dist, dist + 1)
        
 
    # backtrack: remove (i, j) from the visited matrix
    covered = 0
    visited[i][j] = False
    return min_dist
 
# Wrapper over findShortestPath() function
def findShortestPathLength(mat, num):
    if (len(mat) == 0):
        return -1
 
    row = len(mat)
    col = len(mat[0])
 
    # construct an `M × N` matrix to keep track of visited
    # cells
    visited = []
    for i in range(row):
        visited.append([None for _ in range(col)])
 
    dist = sys.maxsize
    dist = findShortestPath(mat, visited, 0, 0, num, dist, 0)
 
    if (dist != sys.maxsize):
        return dist
    return -1
 
# Driver code
mat = [ [0,0,0,1,0,0,1,0,0,0],
        [0,0,0,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,0,1,0],
        [0,0,0,0,1,0,0,0,0,0] ]
 
dist = findShortestPathLength(mat, 20)
print(dist)