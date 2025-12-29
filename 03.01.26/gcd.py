# GCD (Greatest Common Divisor) Calculator in Python

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    result = gcd(abs(num1), abs(num2))
    print(f"GCD of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()
