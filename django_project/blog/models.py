from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 


# each class is its own table in the database and each attribute will be a different field in the database
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(
        default=timezone.now
    )  # sets the current datetime only when a post is added
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if  a user is deleted the post is also deleted 
