from django.db import models

GENDER = (('male','Male'),('female','Female'))

#MODEL STUDENT 
class student(models.Model):
    stdid = models.IntegerField(primary_key=True)    
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    std = models.IntegerField()
    gender = models.CharField(choices= GENDER, default='male',max_length = 100)

    def __str__(self):
        return self.name