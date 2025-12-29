# Linear Search in Python

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def main():
    n = int(input("Enter array size: "))
    arr = []
    
    print("Enter array elements:")
    for i in range(n):
        element = int(input(f"Element {i+1}: "))
        arr.append(element)
    
    target = int(input("\nEnter element to search: "))
    
    index = linear_search(arr, target)
    
    if index != -1:
        print(f"Element {target} found at index {index}")
    else:
        print(f"Element {target} not found in the array")

if __name__ == "__main__":
    main()
