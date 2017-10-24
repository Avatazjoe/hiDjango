from django.http import HttpResponse

import random

def helloWorld (request):

    return HttpResponse("Hello World")

def rootPage(request):
    return HttpResponse("Root Home Page")