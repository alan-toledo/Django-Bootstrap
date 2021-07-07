from django.db import models

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return f'email={self.email}, password={self.password}'

class Priority(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class Status(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #one-to-many
    title = models.CharField(max_length=30)
    priority =  models.ForeignKey(Priority, on_delete=models.CASCADE) #one-to-many
    status =  models.ForeignKey(Status, on_delete=models.CASCADE) #one-to-many
    date = models.DateField() 

    def __str__(self):
        return f'name={self.title}, user_email={self.user.email}'