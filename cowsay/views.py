from django.shortcuts import render
from cowsay.models import CowsayText

# Create your views here.
def index(request):
    text_cowsay = CowsayText.objects.all()
    return render(request, 'index.html', {'text_cowsay': text_cowsay})


#def addtextform(request, text_id):
