from django.db import models
from users.models import userForm
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.timezone import localtime

# Create your models here.
class Blog(models.Model):
    head = models.CharField(max_length=100)
    description = models.TextField()
    # author = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name="blogs")
    published_at = models.DateTimeField(auto_now_add=True)
    blog_image = models.ImageField(null=True, blank= True, upload_to="images/")

    def __str__(self):
        return f"{self.author} created the blog name {self.head}"


class Useractivity(models.Model):
    usernameid = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bloguser",null=True, blank= True)
    postid = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="post",null=True, blank= True)
    commentdes = models.TextField(null=True, blank= True)
    commented_at = models.DateTimeField(auto_now_add=localtime)


    def __self__(self):
        return f"{self.usernameid} has liked the post of {self.postid}"