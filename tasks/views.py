from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Wellcome to the task management system")
def contact(request):
    return HttpResponse("This is contact page")
def resturent(request):
    return HttpResponse("This is resturesnt page")
def show_task(request):
    return HttpResponse("This is our show_task")