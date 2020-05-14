from django.shortcuts import render
from cowsay.models import CowsayTextInput
from cowsay.forms import AddTextForm
from subprocess import PIPE, run

# Create your views here.
def index(req):
    if req.method == "POST":
        form = AddTextForm(req.POST)

        if form.is_valid():
            data = form.cleaned_data
            CowsayTextInput.objects.create(
                cowsay_input=data['add_text']
            )
            command = ['cowsay', data['add_text']]
            result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
            cow = result.stdout
            form = AddTextForm()
            return render(req, 'index.html', {'form': form, 'cow': cow})
    form = AddTextForm()
    return render(req, 'index.html', {'form': form})


def history(req):
    previous_text = CowsayTextInput.objects.all().order_by('-id')[:10]
    return render(req, 'history.html', {"previous_text": previous_text})
