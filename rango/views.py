from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
    html = '''
    <a href='/rango/about'>About</a>
    <p>Rango says hello world</p>
    '''
    return HttpResponse(html)

def about(request):
    html = '''
    <a href='/rango/'>Home</a>
    <p>Rango says here is the about page</p>
    '''
    return HttpResponse(html)    
