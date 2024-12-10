def read_input_file(filepath):
    with open(filepath, "r") as file:
        return file.read()


def calculate_total_distance(input_data):
    left = []
    right = []

    # Parse the input data
    for line in input_data.strip().split('\n'):
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)

    # Sort both lists
    left.sort()
    right.sort()

    # Calculate the total distance
    total_distance = sum(abs(l - r) for l, r in zip(left, right))

    return total_distance


if __name__ == "__main__":
    # Filepath for the input
    input_filepath = "files/1.txt"

    # Read the input data
    input_data = read_input_file(input_filepath)

    # Calculate and print the result
    result = calculate_total_distance(input_data)
    print("Total Distance:", result)
