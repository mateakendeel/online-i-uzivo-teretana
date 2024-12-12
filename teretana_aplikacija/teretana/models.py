from django.db import models
from django.contrib.auth.models import User


class Trainer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Trening(models.Model):
    name=models.CharField(max_length=100)
    trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateTimeField()
    
    def __str__(self):
        return f"{self.name} with {self.trainer.name} for {self.user.username}"

    
class Clanstvo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Membership for {self.user.username} - {'Active' if self.active else 'Inactive'}"

class Vjezba(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in minutes")
    calories_burned = models.IntegerField(help_text="Estimated calories burned")

    def __str__(self):
        return self.name

class PlanTreninga(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    repetitions = models.IntegerField()
    sets = models.IntegerField()

    def _str_(self):
        return f"{self.exercise.name} in {self.workout_plan.title}"
    
class WorkoutPlan(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

