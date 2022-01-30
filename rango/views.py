from django.shortcuts import render

from django.http import HttpResponse

def index(request): #request is a httpResponse object
    #contruct a dictionary to pass to the template engine as it's context
    #note the key boldmessage matches to {{boldmessage}} in the template 
    context_dict ={'boldmessage':'Crunchy, creamy, cookie, candy, cupcake!'}

    #return HttpResponse("Rango says hey there partner! <a href='/rango/'>About</a>") #href defines the url to link to, the text between > and </a> defines the text containing the link

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
     
    context_dict ={'boldmessage':'This tutorial has been put together by David Canavan'}

    return render(request, 'rango/about.html',context=context_dict)

    #return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>") #href defines the url to link to, the text between > and </a> defines the text containing the link
