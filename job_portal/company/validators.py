from django.core.exceptions import ValidationError

def size_validator(value):
    max_size = 5240000 # kb equals 5MB

    if value > max_size:
        raise ValidationError(message='File should not exceeds more than 5MB ')
    

