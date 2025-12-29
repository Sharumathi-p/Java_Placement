# String Reverse in Python

def reverse_string(s):
    return s[::-1]

def reverse_string_manual(s):
    result = ""
    for char in s:
        result = char + result
    return result

def main():
    text = input("Enter a string: ")
    
    # Method 1: Using slicing
    reversed1 = reverse_string(text)
    print(f"\nOriginal string: {text}")
    print(f"Reversed string (using slicing): {reversed1}")
    
    # Method 2: Manual reversal
    reversed2 = reverse_string_manual(text)
    print(f"Reversed string (manual): {reversed2}")

if __name__ == "__main__":
    main()
