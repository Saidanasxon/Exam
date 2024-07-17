import os
from django.core.exceptions import ValidationError

def validate_video_file(value):
    valid_extensions = ['.mp4', '.mov', '.avi', '.mkv']
    ext = os.path.splitext(value.name)[1]
    if ext.lower() not in valid_extensions:
        raise ValidationError('Invalid file format. Allowed formats are: .mp4, .mov, .avi, .mkv')

    filesize = value.size
    if filesize > 1000485760:
        raise ValidationError('File size is too large.')
