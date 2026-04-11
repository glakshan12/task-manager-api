from django.db import models#without this module any models cant create
from django.contrib.auth.models import User#built in features with password,email,usernaem instead of scratch just import it and use this
# Create your models here.
class Task(models.Model):#table name | it should inherit all the table things like save,fetch, and delete as a base class
    STATUS_CHOICES=[#tasks_task is app name + model name
        ('pending','Pending'),#1 store in db and 2nd view of the user nothing just the python list
        ('completed',"Completed"),
    ]#primary id creates automatically
    user=models.ForeignKey(User,on_delete=models.CASCADE)#dajngo woluld automatically add the user_id in database
    title=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    due_date=models.DateField
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='Pending')
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
#makemigrations are instruction for creating the db - reads the models.py file and create it
#migrate are django run those instructions on mysql and create the table -read that migrations file and create the table