
from django import forms


class MemberForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    number = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, min_length=8)
    confirmPassword = forms.CharField(max_length=100, min_length=8)
