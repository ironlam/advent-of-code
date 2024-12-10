def read_input_file(filepath):
    with open(filepath, "r") as file:
        return [list(map(int, line.split())) for line in file.readlines()]


def is_safe(report):
    """
    Determines if a report is safe based on the problem criteria.
    A report is safe if:
    1. All differences between adjacent levels are between 1 and 3.
    2. The levels are either all increasing or all decreasing.
    """
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    # Check if all differences are in the range [1, 3] or [-3, -1]
    if not all(1 <= abs(diff) <= 3 for diff in differences):
        return False

    # Check if the trend is consistent (all positive or all negative)
    if all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences):
        return True

    return False


def count_safe_reports(reports):
    return sum(is_safe(report) for report in reports)


if __name__ == "__main__":
    # Filepath for the input
    input_filepath = "files/2.txt"

    # Read the input data
    reports = read_input_file(input_filepath)

    # Calculate and print the number of safe reports
    safe_count = count_safe_reports(reports)
    print("Number of Safe Reports:", safe_count)
