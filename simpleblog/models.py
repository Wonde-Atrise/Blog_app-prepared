from django.db import models
from django.contrib.auth.models  import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Blogmodel(models.Model):
    title = models.CharField(max_length=100,default="Title")
    description= models.TextField(null=True)
    User_ID =models.ForeignKey(User,on_delete=models.CASCADE)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now_add=True)
    BlogIm= models.ImageField(null=True,blank=True,upload_to='images/')

    Likes = models.ManyToManyField(User, related_name='blog_post', blank=True)
    def total_likes(self):
       return self.Likes.count()
class Message(models.Model):
    blog = models.ForeignKey(Blogmodel,on_delete=models.CASCADE)
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    messageCreated = models.DateTimeField(auto_now_add=True)

    body= models.TextField(default="Messagebody",null=True)
   
class Meta:
    ordering=['-messageCreated']
 
 
 
 
 
class Profile(models.Model):

    Profileowner = models.ForeignKey(User, related_name='userid', on_delete=models.CASCADE)
    Bio = models.TextField(null=True)
    Image = models.ImageField(default="/Userprofile/user.png", blank=True, upload_to='images/')

    def __str__(self):
        return f"Profile for {self.Profileowner.username} (ID: {self.id})" #bett
      
    def __str__(self):
          return super().__str__()
     