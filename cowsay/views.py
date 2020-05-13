from django.shortcuts import render
from cowsay.models import TextLine

# Create your views here.
def index(request):
    text_line = TextLine.objects.all()
    return render(request, 'index.html', {'text_line': text_line})


#def addtextform(request, text_id):
