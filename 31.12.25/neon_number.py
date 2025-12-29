# Neon Number Checker in Python
# A neon number is a number where the sum of digits of square of the number is equal to the number
# Example: 9 is a neon number (9^2 = 81, 8+1 = 9)

def is_neon(num):
    square = num * num
    sum_of_digits = sum(int(digit) for digit in str(square))
    return sum_of_digits == num

def main():
    num = int(input("Enter a number: "))
    
    if is_neon(num):
        print(f"{num} is a Neon number")
        square = num * num
        print(f"{num}^2 = {square}")
        print(f"Sum of digits of {square} = {num}")
    else:
        print(f"{num} is not a Neon number")

if __name__ == "__main__":
    main()
