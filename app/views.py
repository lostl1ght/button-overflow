from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def ask(request):
    return render(request, 'ask.html')

def question(request, id):
    return render(request, 'question.html')

def register(request):
    return render(request, 'register.html')
