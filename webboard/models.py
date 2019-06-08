from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator

# Create your models here.

class Board(models.Model):
    name=models.CharField(max_length=50,unique=True)
    description=models.CharField(max_length=500)
    def __str__(self):
        return self.name
    
    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()

class Topic(models.Model):
    subject=models.CharField(max_length=50)
    last_updated=models.DateTimeField(auto_now_add=True)
    board=models.ForeignKey(Board,related_name='topics',on_delete=models.PROTECT)
    starter=models.ForeignKey(User,related_name='topics',on_delete=models.PROTECT)
    views=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.subject

class Post(models.Model):
    message=models.CharField(max_length=5000)
    topic=models.ForeignKey(Topic,related_name='posts',on_delete=models.PROTECT)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,related_name='posts',on_delete=models.PROTECT)
    updated_at=models.DateTimeField(null=True)
    updated_by=models.ForeignKey(User,related_name='+',null=True,on_delete=models.PROTECT)

    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)



