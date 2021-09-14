from collections import deque


class Cell:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Node:
    def __init__(self, pt: Cell, dist: int):
        self.pt = pt
        self.dist = dist


def is_valid(r, c, tr, tc):
    return (r >= 0) and (r < tr) and (c >= 0) and (c < tc)


# Shortest path in a binary maze where 1 represents obstacle
def shortest_path(maze, src, dest, r, c):
    if maze[src.x][src.y] != 0 or maze[dest.x][dest.y] != 0:
        return -1

    visited = [[False for i in range(c)] for j in range(r)]
    visited[src.x][src.y] = True
    q = deque()
    s = Node(src, 0)
    q.append(s)

    while q:
        current = q.popleft()
        pt = current.pt
        if pt.x == dest.x and pt.y == dest.y:
            return current.dist

        for i in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
            row, col = pt.x + i[0], pt.y + i[1]

            if is_valid(row, col, r, c) and maze[row][col] == 0 and not visited[row][col]:
                visited[row][col] = True
                neighbor = Node(Cell(row, col), current.dist + 1)
                q.append(neighbor)

    return -1


def main():
    maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
    source = Cell(0, 0)
    dest = Cell(3, 3)

    dist = shortest_path(maze, source, dest, len(maze), len(maze[0]))

    if dist != -1:
        print("Shortest Path:", dist)
    else:
        print("No path exists")


main()
