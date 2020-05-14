from django import forms

class addtextform(forms.Form):
    text_line = forms.CharField(widget=forms.Textarea)

