def read_input_file(filepath):
    with open(filepath, "r") as file:
        return [line.strip() for line in file]

def count_x_mas_patterns(grid):
    """
    Counts all valid X-MAS patterns in the grid.
    """
    rows, cols = len(grid), len(grid[0])
    x_mas_count = 0

    def is_valid_position(x, y):
        """Checks if the position is within grid bounds."""
        return 0 <= x < rows and 0 <= y < cols

    def is_valid_x_mas(r, c):
        """
        Checks if the cell at (r, c) is the center of a valid X-MAS pattern.
        """
        if grid[r][c] != "A":
            return False

        # Top-left to bottom-right diagonal (MAS or SAM)
        top_left = (r - 1, c - 1)
        bottom_right = (r + 1, c + 1)

        # Top-right to bottom-left diagonal (MAS or SAM)
        top_right = (r - 1, c + 1)
        bottom_left = (r + 1, c - 1)

        # Ensure all positions are valid
        if not (is_valid_position(*top_left) and is_valid_position(*bottom_right) and
                is_valid_position(*top_right) and is_valid_position(*bottom_left)):
            return False

        # Check if diagonals form valid "MAS" or "SAM" patterns
        diagonal1 = [grid[top_left[0]][top_left[1]], "A", grid[bottom_right[0]][bottom_right[1]]]
        diagonal2 = [grid[top_right[0]][top_right[1]], "A", grid[bottom_left[0]][bottom_left[1]]]

        return (diagonal1 == ["M", "A", "S"] or diagonal1 == ["S", "A", "M"]) and \
               (diagonal2 == ["M", "A", "S"] or diagonal2 == ["S", "A", "M"])

    # Traverse the grid
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if is_valid_x_mas(r, c):
                x_mas_count += 1

    return x_mas_count

if __name__ == "__main__":
    input_filepath = "files/4.txt"  # Path to the input file
    grid = read_input_file(input_filepath)
    x_mas_count = count_x_mas_patterns(grid)
    print("Total X-MAS Patterns:", x_mas_count)
