from django import forms

class AddTextForm(forms.Form):
    add_text = forms.CharField(widget=forms.Textarea)

