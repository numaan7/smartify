from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Subject(models.Model):
    subject_name=models.SlugField(max_length=100,default='Enter subject name.',unique=True)
    
    def __str__(self):
        return self.subject_name

class Year(models.Model):
    year=models.CharField(max_length=50,default='Enter question year.')
    def __str__(self):
        return self.year
    
class Tag(models.Model):
    tag=models.SlugField(unique=True,max_length=100)

class Answer(models.Model):
    answer=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)

class Questions(models.Model):
    url=models.SlugField(unique=True,max_length=100)
    question=models.CharField(max_length=1000)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    answers=models.ManyToManyField(Answer,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    tags = TaggableManager()
    year=models.ForeignKey(Year,on_delete=models.CASCADE,default='2023')
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.question


