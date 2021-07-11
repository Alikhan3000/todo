from django.db import models

class ToDo(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favourite = models.BooleanField(default=False)
    text = models.CharField(max_length=100, default='')

# Create your models here.
