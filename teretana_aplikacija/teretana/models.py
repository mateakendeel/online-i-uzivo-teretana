from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Trening(models.Model):
    name=models.CharField(max_length=100)
    trainer=models.ForeignKey(Trainer, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateTimeField()

def_str_(self):
return f"{self.name}
with{self.trainer.name} for {self.user.username}
