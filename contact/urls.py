from django.urls import path

from contact.views import ContactView, newsletterSubscribe, sendMessage


app_name = 'contact'

urlpatterns = [
   path('', ContactView, name='main-page'),
#    path('subscribe/', newsletterSubscribe, name='newsletter'),
#    path('sendmessage/', sendMessage, name='send-message')
]