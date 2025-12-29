# Count Words in a String in Python

def count_words(text):
    # Strip leading/trailing whitespace and split by whitespace
    words = text.strip().split()
    return len(words)

def count_words_detailed(text):
    words = text.strip().split()
    word_count = len(words)
    char_count = len(text)
    char_count_no_spaces = len(text.replace(" ", ""))
    
    return {
        'words': word_count,
        'characters': char_count,
        'characters_no_spaces': char_count_no_spaces
    }

def main():
    text = input("Enter a string: ")
    
    # Simple count
    word_count = count_words(text)
    print(f"\nNumber of words: {word_count}")
    
    # Detailed count
    stats = count_words_detailed(text)
    print(f"\nDetailed Statistics:")
    print(f"Words: {stats['words']}")
    print(f"Characters (with spaces): {stats['characters']}")
    print(f"Characters (without spaces): {stats['characters_no_spaces']}")

if __name__ == "__main__":
    main()
