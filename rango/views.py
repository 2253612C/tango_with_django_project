from django.shortcuts import render

from django.http import HttpResponse

def index(request): #request is a httpResponse object
    return  HttpResponse("<a href='/rango/about/'>Link to the about page</a>") #string represents the content of the page to send back to the client requesting the view

def about(request):
    return HttpResponse("<a href='/rango/'>Go back to the rango page</a>") #href defines the url to link to, the text between > and </a> defines the text containing the link
