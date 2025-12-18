def get_num_words(string: str) -> int:
    num_words = len(string.split())

    return num_words

def get_char_counts(string: str) -> dict:
    char_counts = {}
    
    for char in string.lower():
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

    return char_counts

def get_sorted_counts(char_counts: dict[str, int])-> list[dict[str, str | int]]:
    sorted_list = [{"char": x[0], "num": x[1]} for x in sorted(char_counts.items(), key=lambda x: -x[1])]

    return sorted_list
