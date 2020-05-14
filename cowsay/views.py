from django.shortcuts import render
from cowsay.models import CowsayTextInput, CowsayTextOutput
from cowsay.forms import AddTextForm
from subprocess import PIPE, run

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = AddTextForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            CowsayTextInput.objects.create(
                cowsay_input=data['inputtext']
            )
            command = ['cowsay', data['inputtext']]
            result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
            cow = result.stdout
            form = AddTextForm()
            return render(request, 'index.html', {'form': form, 'cow': cow})
        form = AddTextForm()
        return render(request, 'index.html', {'form': form})


def history(request):
        updated_text = CowsayTextInput.objects.filter().order_by('-id')[:10]
        return render(request, 'history.html', {'updated_text': updated_text})
