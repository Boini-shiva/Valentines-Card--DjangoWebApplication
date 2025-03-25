from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Card(models.Model):
    name = models.CharField(max_length=25)
    quote = models.TextField()
    propose_date = models.DateTimeField(auto_now_add=True)
    response_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    status = models.BooleanField(blank=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name