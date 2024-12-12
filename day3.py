import re

def read_input_file(filepath):
    with open(filepath, "r") as file:
        return file.read()


def calculate_sum_from_memory(corrupted_memory):
    """
    Scans the corrupted memory for valid mul(X,Y) instructions and returns the sum of their results.
    """
    # Regular expression to match valid mul(X,Y) instructions
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    # Find all matches in the corrupted memory
    matches = re.findall(pattern, corrupted_memory)

    # Calculate the sum of results
    total_sum = 0
    for x, y in matches:
        total_sum += int(x) * int(y)

    return total_sum


if __name__ == "__main__":
    input_filepath = "files/3.txt"
    corrupted_memory = read_input_file(input_filepath)
    result = calculate_sum_from_memory(corrupted_memory)
    print("Total Sum of Valid Multiplications:", result)
