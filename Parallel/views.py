from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view1(request):
    return render(request, 'Parallel/first.html')

def mainpg(request):
    return render(request, 'Parallel/mainpg.html')