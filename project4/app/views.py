from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rejections(request):
    return HttpResponse('rejections successfu')