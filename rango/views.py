from django.shortcuts import render

from django.http import HttpResponse

def index(request): #request is a httpResponse object
    #contruct a dictionary to pass to the template engine as it's context
    #note the key boldmessage matches to {{boldmessage}} in the template 
    context_dict ={'boldmessage':'Crunchy, creamy, cookie, candy, cupcake!'}

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
     
    context_dict ={'boldmessage':'This tutorial has been put together by David Canavan'}

    return render(request, 'rango/index.html',context=context_dict)

    #return HttpResponse("<a href='/rango/'>Go back to the rango page</a>") #href defines the url to link to, the text between > and </a> defines the text containing the link
