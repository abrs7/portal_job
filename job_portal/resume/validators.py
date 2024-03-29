
from django.core.exceptions import ValidationError

def validate_file_size(value):
    """
    Validate the file size against the given MAX_FILE_SIZE value
    """
    max_size = 5242880  # 5 MB limit
    if value.size > max_size:
        raise ValidationError("The file size must not exceed 5 MB")
