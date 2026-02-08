from models import StudentProfile

def validate_types(profile):
    """
    Validates that the StudentProfile fields have correct types.
    Raises TypeError if types are invalid.
    """
    if not isinstance(profile.name, str):
        raise TypeError(f"name must be a string, got {type(profile.name).__name__}")
    if not isinstance(profile.id, int):
        raise TypeError(f"id must be an int, got {type(profile.id).__name__}")
    if not isinstance(profile.grades, list):
        raise TypeError(f"grades must be a list, got {type(profile.grades).__name__}")
    for grade in profile.grades:
        if not isinstance(grade, int):
            raise TypeError(f"each grade must be an int, got {type(grade).__name__}")
