def mines(input_grid):
    grid_len = len(input_grid)
    solution_grid = []

    for row, inner_list in enumerate(input_grid, start=0):
        output_inner_list = []
        for col, val in enumerate(inner_list, start=0):
            if input_grid[row][col] == '#':
                output_inner_list.append('#')
                continue

            total = 0

            #NW
            if row - 1 >= 0 and col - 1 >= 0:
                if input_grid[row - 1][col - 1] == '#':
                    total += 1
            #N
            if row - 1 >= 0:
                if input_grid[row - 1][col] == '#':
                    total += 1

            #NE
            if col + 1 < grid_len and row - 1 >= 0:
                if input_grid[row - 1][col + 1] == '#':
                    total += 1

            #E
            if col + 1 < grid_len:
                if input_grid[row][col + 1] == '#':
                    total += 1

            #SE
            if col + 1 < grid_len and row + 1 < grid_len:
                if input_grid[row + 1][col + 1] == '#':
                    total += 1

            #S
            if row + 1 < grid_len:
                if input_grid[row + 1][col] == '#':
                    total += 1

            #SW
            if row + 1 < grid_len and col - 1 >= 0:
                if input_grid[row + 1][col - 1] == '#':
                    total += 1

            #W
            if col - 1 >= 0:
                if input_grid[row][col - 1] == '#':
                    total += 1


            output_inner_list.append(str(total))
        solution_grid.append(output_inner_list)

    return solution_grid

if __name__ == '__main__':
    input_grid = [['#', '-', '-', '-', '#'],
                  ['-', '-', '#', '-', '-'],
                  ['-', '-', '#', '-', '#'],
                  ['#', '-', '-', '#', '-'],
                  ['-', '-', '-', '-', '#']]
    print("Input grid:")
    for row in input_grid:
        print(*row, sep="\t")

    solution_grid = mines(input_grid)
    print("\nSolution grid:")
    for row in solution_grid:
        print(*row, sep="\t")

