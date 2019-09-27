from django import forms
from aptude.validators import validate_file_extension


class MainForm(forms.Form):
    file = forms.FileField(allow_empty_file=False, validators=[validate_file_extension])
