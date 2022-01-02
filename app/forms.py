from django.forms import ModelForm
from.models import Hood, User
from django.contrib.auth.forms import UserCreationForm



class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


        
class HoodForm(ModelForm):
    class Meta:
        model = Hood
        fields = '__all__'
        exclude = ['host', 'occupants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name','username','email','profile_pic','bio']
