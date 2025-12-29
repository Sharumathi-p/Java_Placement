# Star Pattern 2 in Python

def print_star_pattern_2(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

def main():
    n = int(input("Enter number of rows: "))
    print_star_pattern_2(n)

if __name__ == "__main__":
    main()
