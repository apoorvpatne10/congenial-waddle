from django import forms
from .models import MyModel


class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ('file_name', 'my_file')


class MyModelUpdateForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ('file_name', 'my_file')
