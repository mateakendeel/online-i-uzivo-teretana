from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView
from django.db.models import Q 
from teretana.models import Trening

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
    trenings = Trening.objects.filter(user=request.user)
    return render(request, 'user_home.html', {'trenings': trenings})
def home(request):
    return render(request, 'home.html') 

class TreningListView(ListView):
    model = Trening
    template_name = 'trening_list.html'
    context_object_name = 'trenings'
    paginate_by = 10 

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(trainer__name__icontains=query) |
                Q(user__username__icontains=query)
            )
        return queryset


class TreningDetailView(DetailView):
    model = Trening
    template_name = 'trening_detail.html'
    context_object_name = 'trening'