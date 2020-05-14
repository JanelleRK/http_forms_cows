from django.shortcuts import render
from cowsay.models import CowsayTextInput, CowsayTextOutput
from cowsay.forms import addtextform

# Create your views here.
def index(request):
    text_cowsay = CowsayTextInput.objects.all()
    return render(request, 'index.html', {'text_cowsay': text_cowsay})


