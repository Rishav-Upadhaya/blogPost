from django.db import models
from users.models import userForm
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    head = models.CharField(max_length=100)
    description = models.TextField()
    # author = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name="blogs")
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} created the blog name {self.head} which is described as {self.description} at {self.published_at}"
