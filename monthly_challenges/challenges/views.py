from django.shortcuts import render
from django.http import HttpResponse

# Creating a First View & URL

def index(request):
  return HttpResponse("This Works!")


# Create your views here.
