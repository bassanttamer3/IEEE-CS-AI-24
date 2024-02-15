def count_word_occurrences(file_path):
    word_counts = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
    return word_counts
def print_word_occurrences(word_counts):
    for word, count in word_counts.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    try:
        word_counts = count_word_occurrences(file_path)
        print("\nWord occurrences in the file:")
        print_word_occurrences(word_counts)
    except FileNotFoundError:
        print("File not found. Please enter a valid file path.")
