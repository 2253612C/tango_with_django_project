from django.shortcuts import render

from django.http import HttpResponse

def index(request): #request is a httpResponse object
    return  HttpResponse("Rango says hey there partner!") #string represents the content of the page to send back to the client requesting the view
