# Grade Calculator in Python

def calculate_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    elif marks >= 50:
        return 'E'
    else:
        return 'F'

def main():
    print("Grade Calculator")
    print("-" * 30)
    
    num_subjects = int(input("Enter number of subjects: "))
    total = 0
    
    for i in range(num_subjects):
        marks = float(input(f"Enter marks for subject {i+1}: "))
        total += marks
    
    average = total / num_subjects
    grade = calculate_grade(average)
    
    print(f"\nTotal Marks: {total}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
