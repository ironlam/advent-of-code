def read_input_file(filepath):
    with open(filepath, "r") as file:
        return [line.strip() for line in file]


def count_word_occurrences(grid, word):
    """
    Counts the number of times the word appears in the grid in all directions.
    """
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    directions = [
        (0, 1),  # Horizontal: left-to-right
        (0, -1),  # Horizontal: right-to-left
        (1, 0),  # Vertical: top-to-bottom
        (-1, 0),  # Vertical: bottom-to-top
        (1, 1),  # Diagonal: top-left to bottom-right
        (-1, -1),  # Diagonal: bottom-right to top-left
        (1, -1),  # Diagonal: top-right to bottom-left
        (-1, 1),  # Diagonal: bottom-left to top-right
    ]
    count = 0

    def is_valid_position(x, y):
        return 0 <= x < rows and 0 <= y < cols

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                # Check if "word" fits in the current direction
                if all(
                        is_valid_position(r + i * dr, c + i * dc) and
                        grid[r + i * dr][c + i * dc] == word[i]
                        for i in range(word_length)
                ):
                    count += 1

    return count


if __name__ == "__main__":
    input_filepath = "files/4.txt"
    grid = read_input_file(input_filepath)
    word = "XMAS"
    occurrences = count_word_occurrences(grid, word)
    print("Total Occurrences of 'XMAS':", occurrences)
