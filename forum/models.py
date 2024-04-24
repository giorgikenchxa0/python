from django.db import models
from django.conf import settings
#from django.conf import Settings

# Create your models here.


class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length = 101)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    

   
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add = True)
    modify_date = models.DateTimeField(auto_now =True)


