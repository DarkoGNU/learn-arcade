import re

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def binary_search(array, key, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if start > end:
        return -1

    mid = (start + end) // 2

    if key == array[mid]:
        return mid
    elif key < array[mid]:
        return binary_search(array, key, start, mid - 1)
    else:
        return binary_search(array, key, mid + 1, end)


def main():
    with open("dictionary.txt") as file:
        dictionary = tuple(line.strip().lower() for line in file)

    print("--- Linear Search ---")

    with open("AliceInWonderLand200.txt") as file:
        for i, line in enumerate(file):
            word_list = split_line(line)
            for word in word_list:
                pos = 0
                while pos < len(dictionary) and dictionary[pos] != word.lower():
                    pos += 1

                if pos >= len(dictionary):
                    print(f"Line {i:3}: possibly misspelled word: {word}")

    print("--- Binary Search ---")

    with open("AliceInWonderLand200.txt") as file:
        for i, line in enumerate(file):
            word_list = split_line(line)
            for word in word_list:
                if binary_search(dictionary, word.lower()) == -1:
                    print(f"Line {i:3}: possibly misspelled word: {word}")

if __name__ == "__main__":
    main()
