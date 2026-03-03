import heapq
import math

# ------------------ Heuristic Functions ------------------

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def euclidean(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# ------------------ A* Algorithm ------------------

def astar(maze, start, goal, heuristic_type="manhattan"):
    rows = len(maze)
    cols = len(maze[0])

    open_list = []
    heapq.heappush(open_list, (0, start))

    g_score = {start: 0}
    came_from = {}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(came_from, current)

        # 4-direction movement (up, down, left, right)
        neighbors = [
            (current[0] + 1, current[1]),
            (current[0] - 1, current[1]),
            (current[0], current[1] + 1),
            (current[0], current[1] - 1),
        ]

        for neighbor in neighbors:
            r, c = neighbor

            # Check boundaries and walls
            if 0 <= r < rows and 0 <= c < cols and maze[r][c] != '#':
                tentative_g = g_score[current] + 1

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g

                    # Choose heuristic
                    if heuristic_type == "manhattan":
                        h = manhattan(neighbor, goal)
                    else:
                        h = euclidean(neighbor, goal)

                    f_score = tentative_g + h
                    heapq.heappush(open_list, (f_score, neighbor))
                    came_from[neighbor] = current

    return None  # If no path found

# ------------------ Path Reconstruction ------------------

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

# ------------------ Print Maze ------------------

def print_maze_with_path(maze, path):
    maze_copy = [row[:] for row in maze]

    for r, c in path:
        if maze_copy[r][c] not in ('S', 'G'):
            maze_copy[r][c] = '*'

    for row in maze_copy:
        print(" ".join(row))

# ------------------ Example Maze ------------------

maze = [
    ['S', '.', '.', '#', '.', '.'],
    ['#', '#', '.', '#', '.', '#'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '#', '.'],
    ['.', '.', '.', '.', 'G', '.']
]

# Find start and goal positions
start = None
goal = None

for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == 'S':
            start = (i, j)
        elif maze[i][j] == 'G':
            goal = (i, j)

# Run A*
path = astar(maze, start, goal, heuristic_type="manhattan")

# Output Result
if path:
    print("Shortest Path Found:")
    print(path)
    print("\nMaze with Path:")
    print_maze_with_path(maze, path)
else:
    print("Goal is unreachable from the start position.")