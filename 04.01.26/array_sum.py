# Array Sum Calculator in Python

def array_sum(arr):
    return sum(arr)

def main():
    n = int(input("Enter array size: "))
    arr = []
    
    print("Enter array elements:")
    for i in range(n):
        element = int(input(f"Element {i+1}: "))
        arr.append(element)
    
    total = array_sum(arr)
    print(f"\nArray: {arr}")
    print(f"Sum of array elements: {total}")

if __name__ == "__main__":
    main()
