from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Trainer, WorkoutPlan, Exercise, PlanTreninga, Trening, Clanstvo, Vjezba
from django.urls import reverse_lazy
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


class GenericListView(ListView):
    template_name = 'generic_list.html'
    context_object_name = 'objects'
    paginate_by = 10

    def get_queryset(self):
        model_name = self.kwargs.get('model')
        query = self.request.GET.get('q')
        model = {
            'trainer': Trainer,
            'workoutplan': WorkoutPlan,
            'exercise': Exercise,
            'plantreninga': PlanTreninga,
            'trening': Trening,
            'clanstvo': Clanstvo,
            'vjezba': Vjezba,
        }.get(model_name)

        if model:
            queryset = model.objects.all()
            if query:
                
                if model_name == 'trainer':
                    queryset = queryset.filter(Q(name__icontains=query) | Q(email__icontains=query))
                elif model_name == 'workoutplan':
                    queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query))
                elif model_name == 'exercise':
                    queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query))
                elif model_name == 'plantreninga':
                    queryset = queryset.filter(Q(workout_plan__name__icontains=query) | Q(exercise__name__icontains=query))
                elif model_name == 'trening':
                    queryset = queryset.filter(Q(name__icontains=query) | Q(trainer__name__icontains=query) | Q(user__username__icontains=query))
                elif model_name == 'clanstvo':
                    queryset = queryset.filter(Q(user__username__icontains=query) | Q(start_date__icontains=query) | Q(end_date__icontains=query))
                elif model_name == 'vjezba':
                    queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query))
            return queryset
        return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_name = self.kwargs.get('model')
        context['model_name'] = model_name 
        return context

class GenericDetailView(DetailView):
    template_name = 'generic_detail.html'
    context_object_name = 'object'

    def get_queryset(self):
        model_name = self.kwargs.get('model')
        model = {
            'trainer': Trainer,
            'workoutplan': WorkoutPlan,
            'exercise': Exercise,
            'plantreninga': PlanTreninga,
            'trening': Trening,
            'clanstvo': Clanstvo,
            'vjezba': Vjezba,
        }.get(model_name)
        if model:
            return model.objects.all()
        return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_name = self.kwargs.get('model')
        context['model_name'] = model_name  
        return context
