from django.contrib import admin
from contact.forms import SubscriberForm
from contact.models import Receipient, Subscriber
from accounts.admin import user_admin

# Register your models here.
admin.site.register(Receipient)
user_admin.register(Receipient)