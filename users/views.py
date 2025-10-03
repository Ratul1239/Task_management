from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.form import register_form,userregister_form
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse
# Create your views here.
def sing_up(request):
    if request.method=='GET':
        form=userregister_form()
    if request.method=='POST':
        form=userregister_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sing-up')
        else:
            print("password are not same")
    return render(request,'register/sing-up.html',{"form":form})

def sing_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('user-dashbord')
        else:
            return HttpResponse("Invalid username or password")

    return render(request, 'register/login.html')
def sing_out(request):
    logout(request)  
    return redirect('sing-in')