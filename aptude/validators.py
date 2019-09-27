from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage


def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.xls', '.csv']

    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')
