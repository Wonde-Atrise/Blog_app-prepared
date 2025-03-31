from django.forms import ModelForm, forms
from .models import Blogmodel
from django.contrib.auth.models import User
 
    
class Blogdetails(ModelForm):
     class Meta:
         model = Blogmodel
         fields= ['title', 'description']


    
class BlogForm(ModelForm):
     class Meta:
         model = Blogmodel
         fields= ['title', 'description','BlogIm']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [ 'username', 'email']
        
