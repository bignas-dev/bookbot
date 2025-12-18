from stats import get_num_words, get_char_counts, get_sorted_counts
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

print("============ BOOKBOT ============")

with open(book_path, encoding="utf-8") as f:
    file_contents = f.read()

print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")

num_words = get_num_words(file_contents)
print(f"Found {num_words} total words")

print("--------- Character Count -------")
char_counts = get_char_counts(file_contents)
sorted_char_counts = get_sorted_counts(char_counts)

for char_data in sorted_char_counts:
    print(f"{char_data['char']}: {char_data['num']}")

print("============= END ===============")
