# Print Numbers in Different Patterns in Python

def print_numbers_pattern(n):
    print("Pattern 1: Sequential numbers")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    
    print("\nPattern 2: Same number in each row")
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=" ")
        print()

def main():
    n = int(input("Enter number of rows: "))
    print_numbers_pattern(n)

if __name__ == "__main__":
    main()
