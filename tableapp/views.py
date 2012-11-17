from  models import *
from django.shortcuts import render_to_response
from django.http import HttpResponse

def main(request):
    f = Person.object.all()
    print f
    return HttpResponse("Hello")
    
