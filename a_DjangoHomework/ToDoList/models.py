from django.db import models


# Create your models here.
class ToDoList(models.Model):
    content = models.CharField(max_length=200)
    set_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
