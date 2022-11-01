from django.core.exceptions import ValidationError

def validate_file_size(value):
    filesize= value.size
    if filesize > 2097152:
        raise ValidationError(f'You cannot upload file more than 2Mb')
    else:
        return value