from django.shortcuts import render
from rango.models import Category
from rango.models import Page

from django.http import HttpResponse

def index(request): #request is a httpResponse object
    category_list = Category.objects.order_by('-likes')[:5] #get the 5 most liked categories

    page_list = Page.objects.order_by('-views')[:5] #get the 5 most liked categories
    
    context_dict = {}
    context_dict['boldmessage']='Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories']=category_list
    context_dict['pages']=page_list
    

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
     
    context_dict ={'boldmessage':'This tutorial has been put together by David Canavan'}

    return render(request, 'rango/about.html',context=context_dict)

    #return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>") #href defines the url to link to, the text between > and </a> defines the text containing the link


def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # The .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)
        
        # Retrieve all of the associated pages.
        # The filter() will return a list of page objects or an empty list.
        pages = Page.objects.filter(category=category)
       
        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        
        # We also add the category object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        
        context_dict['category'] = category
        
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
       
        context_dict['category'] = None
        context_dict['pages'] = None
      
    # Go render the response and return it to the client.
    return render(request, 'rango/category.html', context=context_dict)