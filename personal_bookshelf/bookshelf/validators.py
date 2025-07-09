from django.core.exceptions import ValidationError
import os

def validate_image_extension(value):
    ext = os.path.splitext(value.name)[1].lower()
    valid_extensions = ['.jpg', '.jpeg', '.png']
    if ext not in valid_extensions:
        raise ValidationError(
            f'Unsupported file extension: {ext}. Please upload a JPG or PNG image.'
        )
