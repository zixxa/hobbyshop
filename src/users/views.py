from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from src.users.forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
       form = SignUpForm(request.POST) 
       if form.is_valid():
           user = form.save()
           user.refresh_from_db()
           username = form.cleaned_data.get('username')
           email = form.cleaned_data.get('email')
           user.save()
           password = form.cleaned_data.get('password1')
           user = authenticate(username=username, password=password)
           login(request, user)
           return redirect('/')

    else:
        form = SignUpForm()

    return render(request, 'users/register.html', {'form': form})
