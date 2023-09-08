from django.forms import ModelForm

from contact.models import Subscriber

class SubscriberForm(ModelForm):
   class Meta:
      model = Subscriber
      fields = '__all__'