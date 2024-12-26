from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
  
    class Meta:
        abstract = True  

class Trainer(BaseModel):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class WorkoutPlan(BaseModel):
    description = models.TextField()

    def __str__(self):
        return self.name

class Exercise(BaseModel):
    description = models.TextField()

    def __str__(self):
        return self.name

class PlanTreninga(BaseModel):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    repetitions = models.IntegerField()
    sets = models.IntegerField()

    def __str__(self):
        return f"{self.exercise.name} in {self.workout_plan.name}"

class Trening(BaseModel):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} with {self.trainer.name} for {self.user.username}"

class Clanstvo(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Membership for {self.user.username} - {'Active' if self.active else 'Inactive'}"

class Vjezba(BaseModel):
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in minutes")
    calories_burned = models.IntegerField(help_text="Estimated calories burned")

    def __str__(self):
        return self.name
