from collections import Counter

def read_input_file(filepath):
    left, right = [], []
    with open(filepath, "r") as file:
        for line in file:
            l, r = map(int, line.split())
            left.append(l)
            right.append(r)
    return left, right


def calculate_similarity_score(left_list, right_list):
    """
    Calculates the similarity score based on the frequency of numbers
    from the left list appearing in the right list.
    """
    # Count the frequencies of each number in the right list
    right_counts = Counter(right_list)

    # Calculate the similarity score
    similarity_score = 0
    for num in left_list:
        similarity_score += num * right_counts.get(num, 0)

    return similarity_score


if __name__ == "__main__":
    input_filepath = "files/1.txt"
    left_list, right_list = read_input_file(input_filepath)
    similarity_score = calculate_similarity_score(left_list, right_list)
    print("Similarity Score:", similarity_score)
