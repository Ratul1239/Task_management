from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.form import register_form,userregister_form
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from users.form import MyAuthForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
# Create your views here.
def sing_up(request):
    if request.method=='GET':
        form=userregister_form()
    if request.method=='POST':
        form=userregister_form(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data.get('password1'))
            user.is_active=False
            user.save()
            messages.success(request,'A confirmation mail sent. Plase cheak your email')
            return redirect('sing-in')
        else:
            print("password are not same")
    return render(request,'register/sing-up.html',{"form":form})

def sing_in(request):
    if request.method == 'POST':
        form = MyAuthForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = MyAuthForm()

    return render(request, 'register/login.html',{'form':form})
def sing_out(request):
    logout(request)  
    return redirect('sing-in')


def activate_user(request, user_id, token):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        messages.error(request, "Invalid user.")
        return redirect('sing-in')

    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Account activated successfully! Please sign in.")
    else:
        messages.error(request, "Invalid or expired activation link.")
    
    return redirect('sing-in')
