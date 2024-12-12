from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login


from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_group, created = Group.objects.get_or_create(name='User')
            user.groups.add(user_group)

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')  
            user = authenticate(username=username, password=password) 
            if user is not None:
                login(request, user)  
                return redirect('user_home')  
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def is_admin(user):
    return user.groups.filter(name='Administrator').exists()

@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required
def user_home(request):
    return render(request, 'user_home.html')

def home(request):
    return render(request, 'home.html') 