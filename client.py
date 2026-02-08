from models import StudentProfile
from server import calculate_grade_average

# Example student
student1 = StudentProfile("Alice", 101, [90, 80, 70])
average1 = calculate_grade_average(student1)
print(f"{student1.name}'s average grade is {average1}")

# Example with invalid data (will raise TypeError)
try:
    student2 = StudentProfile("Bob", "102", [85, 75, 95])  # id should be int
    calculate_grade_average(student2)
except TypeError as e:
    print(f"TypeError caught: {e}")
