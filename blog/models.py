from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
      return self.user.username



class Blog(models.Model):
    title = models.CharField(max_length=100, null = False, default="")
    subtitle = models.CharField(max_length=200, default="")
    publish_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/', default="", null=True)
    photo_caption = models.TextField(default = 'Imaages By owner', null = True)
    body = MarkdownxField()
 
    def summary(self):
        return self.body[:100]
    def pub_date_pretty(self):
        return self.publish_date.strftime('%b %e, %Y')
    
    def formatted_markdown(self):
        return markdownify(self.body)
    
    def __str__(self):
        return self.title


class Comment(models.Model):

    blog = models.ForeignKey(Blog, on_delete = models.CASCADE, related_name = 'comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    creadted = models.DateTimeField(auto_now_add = True)
    active = models.BooleanField(default = True)

    class Meta:
        ordering = ('creadted',)

    def __str__(self):
        return f'Comment by {self.name} on {self.blog}'
        
