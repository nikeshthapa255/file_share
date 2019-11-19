from django import forms
from .models import Ufile



class UfileForm(forms.ModelForm):
    class Meta:
        model = Ufile
        fields = ("name", "fileloc",)
        # fields = '__all__'
    