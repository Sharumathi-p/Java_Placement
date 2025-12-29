# Sum of Digits in Python

def sum_of_digits(num):
    num = abs(num)
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

def main():
    num = int(input("Enter a number: "))
    result = sum_of_digits(num)
    print(f"Sum of digits of {num}: {result}")

if __name__ == "__main__":
    main()
