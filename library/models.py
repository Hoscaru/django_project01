from django.db import models

# Create your models here.


class Book(models.Model):
    
    title=models.CharField(max_length=20)
    body=models.TextField()
    author=models.CharField(max_length=50)
    pages=models.IntegerField()
    Year=models.DateField()

    def __str__(self):
        
        name=self.title
        return name