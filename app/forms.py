from django.forms import ModelForm
from.models import Hood

class HoodForm(ModelForm):
    class Meta:
        model = Hood
        fields = '__all__'