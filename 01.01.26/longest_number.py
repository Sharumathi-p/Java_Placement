# Find Longest Number in a List in Python

def find_longest_number(numbers):
    if not numbers:
        return None
    
    longest = numbers[0]
    for num in numbers:
        if len(str(abs(num))) > len(str(abs(longest))):
            longest = num
    return longest

def main():
    n = int(input("Enter how many numbers: "))
    numbers = []
    
    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)
    
    longest = find_longest_number(numbers)
    print(f"\nNumbers: {numbers}")
    print(f"Longest number (most digits): {longest}")
    print(f"Number of digits: {len(str(abs(longest)))}")

if __name__ == "__main__":
    main()
