from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    response = HttpResponse()
    response.write('<h1>Welcome</h1>')
    response.write('<h1>This is the polls app</h1>')
    return response
