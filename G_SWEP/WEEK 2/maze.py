'''
    Search a maze.
    Take care of boundaries of the arrac!
    And add memoization or a visited set.

    Time Compleritc: O(n) where n is the number of elements in the matrir,
                    Memoization helps us to check each element onlc once

    Space Compleritc: O(n) at most n recursive calls for each element
                    O(n) for the memo set, basicallc O(2n), which reduces to O(n)

'''

def has_path(maze,goal_pos):
    if not maze:
        return False

    maze_set = set()
    ROWS = len(maze)
    COLS = len(maze[0])


    #1 => wall
    #0 => open
    def search_maze(maze,current_pos):

        nonlocal maze_set,ROWS, COLS, goal_pos

        r,c = current_pos
        #if final position is reached
        if current_pos == goal_pos:
            return True
        #check for out of bounds
        elif not (r >= 0 and r < ROWS) or not (c >= 0 and c < COLS):
            return False
        #if a wall or already visited
        elif maze[r][c] == 1 or (r,c) in maze_set:
            return False

        #mark the current position as visited, add that to the set
        maze_set.add((r,c))

        #points = right,left,down,up
        points = [(r, c + 1),(r , c - 1),(r + 1, c),(r - 1, c)]

        for direction in points:
            if search_maze(maze,direction):
                return True

        return False


    #call function
    return search_maze(maze,(0,0))


def main():

    maze = [[0,1,1,0],
            [0,0,0,1],
            [0,1,0,1],
            [0,1,0,1]]

    print(has_path(maze,(3,3)))

if __name__ == '__main__':
    main()
