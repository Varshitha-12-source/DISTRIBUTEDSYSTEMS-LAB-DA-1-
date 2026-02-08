# DA-1: Python RPC Framework Lab

## Features Implemented

- Created `StudentProfile` object with:
  - `name` (string)
  - `id` (int)
  - `grades` (list of integers)
- Implemented `calculate_grade_average(StudentProfile profile)` to calculate the average grade.
- Implemented `validate_types(profile)` function in the marshalling layer:
  - Checks that `name` is string, `id` is int, and `grades` is a list of integers.
  - Raises `TypeError` if the types are incorrect.

## Test Results

### Valid Input

```python
student1 = StudentProfile("Alice", 101, [90, 80, 70])
average1 = calculate_grade_average(student1)
print(f"{student1.name}'s average grade is {average1}")
