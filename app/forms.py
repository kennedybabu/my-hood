from django.forms import ModelForm
from.models import Hood
from django.contrib.auth.models import User

class HoodForm(ModelForm):
    class Meta:
        model = Hood
        fields = '__all__'
        exclude = ['host', 'occupants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
