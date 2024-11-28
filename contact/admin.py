from django.contrib import admin
from contact.forms import SubscriberForm
from contact.models import Receipient, Subscriber
from accounts.admin import user_admin
from unfold.admin import ModelAdmin

@admin.register(Receipient)
class ReceipientAdminClass(ModelAdmin):
    pass

user_admin.register(Receipient)