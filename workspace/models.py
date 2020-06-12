from django.db import models

# Create your models here.


class Addworkplace(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title



class Addtask(models.Model):
    tname = models.ForeignKey(Addworkplace, on_delete=models.CASCADE, related_name='workplace')
    task = models.CharField(max_length=100)
    discriptions = models.TextField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.task