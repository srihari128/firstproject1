from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vanjakalyan(request):
    return HttpResponse('<h1><marquee>Bapu is Best competitor of Johnysins</marquee></h1>')
