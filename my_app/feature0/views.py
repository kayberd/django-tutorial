from django.http import HttpResponse
from django.shortcuts import render
from . models import Feature

def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'Our service is very quick'
    feature1.is_true = True
    
    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Fast 2'
    feature2.details = 'Our service is very quick 2'
    feature2.is_true = False
    
    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Fast 3'
    feature3.details = 'Our service is very quick 3 '
    feature3.is_true = True
    
    featureList = [feature1, feature2, feature3]
    context = {
        'features': featureList
    }
    return render(request, 'index.html', context)

def counter(request):
    text = request.POST['text']
    num_of_words = len(text.split())
    context = {'num_of_words': num_of_words}
    return render(request, 'counter.html', context)