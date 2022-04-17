from django import forms
from django.forms import fields
from app.models import Employee
class display(forms.Form):
    Name=forms.CharField(max_length=25,label="Name")
    Position=forms.CharField(max_length=20,label="Position")
    Age=forms.CharField(max_length=20,label="Age")

class display1(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"
