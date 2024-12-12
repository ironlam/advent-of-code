import re

def read_input_file(filepath):
    with open(filepath, "r") as file:
        return file.read()


def calculate_sum_with_conditions(corrupted_memory):
    """
    Scans the corrupted memory for valid mul(X,Y) instructions, respecting do() and don't().
    Returns the sum of results from enabled multiplications.
    """
    # Regular expressions for mul, do, and don't
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    condition_pattern = r"do\(\)|don't\(\)"

    # Initialize variables
    total_sum = 0
    enabled = True  # Multiplications are enabled at the start

    # Split input into tokens that are either mul or condition instructions
    tokens = re.split(f"({mul_pattern}|{condition_pattern})", corrupted_memory)

    for token in tokens:
        if not token:
            continue

        # Handle `do()` and `don't()`
        if token == "do()":
            enabled = True
        elif token == "don't()":
            enabled = False

        # Handle valid `mul(X,Y)`
        else:
            match = re.match(mul_pattern, token)
            if match and enabled:
                x, y = map(int, match.groups())
                total_sum += x * y

    return total_sum


if __name__ == "__main__":
    input_filepath = "files/3.txt"
    corrupted_memory = read_input_file(input_filepath)
    result = calculate_sum_with_conditions(corrupted_memory)
    print("Total Sum with Conditions:", result)
