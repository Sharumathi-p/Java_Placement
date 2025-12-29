# Power of a Number in Python

def power(base, exp):
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / power(base, -exp)
    else:
        result = 1
        for _ in range(exp):
            result *= base
        return result

def main():
    base = int(input("Enter base: "))
    exp = int(input("Enter exponent: "))
    
    result = power(base, exp)
    print(f"{base} raised to power {exp} is: {result}")

if __name__ == "__main__":
    main()
