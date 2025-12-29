# Dictionary Operations in Python

def main():
    # Create a dictionary
    student = {
        'name': 'John',
        'age': 20,
        'grade': 'A',
        'subjects': ['Math', 'Physics', 'Chemistry']
    }
    
    print("Student Dictionary:")
    print(student)
    
    # Access elements
    print(f"\nName: {student['name']}")
    print(f"Age: {student['age']}")
    
    # Add new key-value pair
    student['email'] = 'john@example.com'
    print(f"\nAfter adding email: {student}")
    
    # Update value
    student['age'] = 21
    print(f"After updating age: {student}")
    
    # Remove element
    del student['grade']
    print(f"After removing grade: {student}")
    
    # Iterate through dictionary
    print("\nIterating through dictionary:")
    for key, value in student.items():
        print(f"{key}: {value}")
    
    # Check if key exists
    if 'name' in student:
        print(f"\n'name' exists in dictionary")

if __name__ == "__main__":
    main()
