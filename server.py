from models import StudentProfile
from rpc_framework import validate_types

def calculate_grade_average(profile: StudentProfile) -> float:
    """
    Remote function to calculate the average grade of a student.
    """
    validate_types(profile)  # Ensure the data is valid

    if not profile.grades:
        return 0.0
    return sum(profile.grades) / len(profile.grades)
