from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    
    ## auto_now = true == Update with current time and date 
        ## auto_now_add = true == Save the time with the time of creation 

    author = models.ForeignKey(User,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title
    
    