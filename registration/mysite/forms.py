from django import forms

class CourForm(forms.Form):
    Title = forms.CharField(label="Titre", max_length=100)
    slug = forms.CharField(label="Description", widget=forms.Textarea)
    content = forms.CharField(label="Contenu", widget=forms.Textarea)