from django import forms
from core.models import ExcelFile


class ExcelForm(forms.ModelForm):
    class Meta:
        model = ExcelFile
        fields = ('file_name',)
