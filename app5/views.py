from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def f1(request):
    return HttpResponse("Hello There")
def f2(req):
    return render(req,'welcome.html')
