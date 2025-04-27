from django.http import HttpResponse
from django.shortcuts import render
from . models import Feature

def index(request):
    features = Feature.objects.all()

    context = {
        'features': features
    }
    return render(request, 'index.html', context)

def counter(request):
    text = request.POST['text']
    num_of_words = len(text.split())
    context = {'num_of_words': num_of_words}
    return render(request, 'counter.html', context)