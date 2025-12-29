# Swap Two Numbers in Python

def swap_with_temp(a, b):
    print(f"Before swap: a = {a}, b = {b}")
    temp = a
    a = b
    b = temp
    print(f"After swap: a = {a}, b = {b}")

def swap_without_temp(a, b):
    print(f"\nBefore swap: a = {a}, b = {b}")
    a = a + b
    b = a - b
    a = a - b
    print(f"After swap: a = {a}, b = {b}")

def swap_pythonic(a, b):
    print(f"\nBefore swap: a = {a}, b = {b}")
    a, b = b, a
    print(f"After swap: a = {a}, b = {b}")

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    print("\nMethod 1: Using temporary variable")
    swap_with_temp(num1, num2)
    
    print("\nMethod 2: Without temporary variable")
    swap_without_temp(num1, num2)
    
    print("\nMethod 3: Pythonic way")
    swap_pythonic(num1, num2)

if __name__ == "__main__":
    main()
