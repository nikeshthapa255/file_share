from django import forms
from .models import Afile



class AfileForm(forms.ModelForm):
    class Meta:
        model = Afile
        # fields = ("name", "fileloc",)
        fields = '__all__'
    