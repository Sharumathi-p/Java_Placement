# Star Pattern 1 in Python

def print_star_pattern_1(n):
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()

def main():
    n = int(input("Enter number of rows: "))
    print_star_pattern_1(n)

if __name__ == "__main__":
    main()
