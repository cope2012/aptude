from django import forms
from aptude.validators import validate_image_file_extension


def home_page_path(instance, filename):
    return f'main/{instance.id}-{filename}'


class MainForm(forms.Form):
    file = forms.FileField(allow_empty_file=False, validators=[validate_image_file_extension])
