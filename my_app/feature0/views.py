from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def counter(request):
    text = request.POST['text']
    num_of_words = len(text.split())
    context = {'num_of_words': num_of_words}
    return render(request, 'counter.html', context)