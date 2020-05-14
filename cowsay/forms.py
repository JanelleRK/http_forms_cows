from django import forms

class AddTextForm(forms.Form):
    text_line = forms.CharField(widget=forms.Textarea)

