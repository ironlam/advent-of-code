def read_input_file(filepath):
    with open(filepath, "r") as file:
        return [list(map(int, line.split())) for line in file.readlines()]


def is_safe(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    # Check if all differences are in the range [1, 3] or [-3, -1]
    if not all(1 <= abs(diff) <= 3 for diff in differences):
        return False

    # Check if the trend is consistent (all positive or all negative)
    if all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences):
        return True

    return False


def can_be_safe_with_one_removal(report):
    for i in range(len(report)):
        # Create a new report by skipping the ith level
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True
    return False


def count_safe_reports(reports):
    safe_count = 0
    for report in reports:
        if is_safe(report) or can_be_safe_with_one_removal(report):
            safe_count += 1
    return safe_count


if __name__ == "__main__":
    # Filepath for the input
    input_filepath = "files/2.txt"

    # Read the input data
    reports = read_input_file(input_filepath)

    # Calculate and print the number of safe reports
    safe_count = count_safe_reports(reports)
    print("Number of Safe Reports with Problem Dampener:", safe_count)
