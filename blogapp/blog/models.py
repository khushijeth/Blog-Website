from django.db import models 
# This is the recommended approach because it links each blog to a real registered user.
# We'll introduce this after we implement user authentication, so it makes sense conceptually.
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blogs"
    )
    image=models.ImageField(upload_to='blog_imaes/')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    