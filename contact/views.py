from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

from django.template.loader import render_to_string
from django.utils.html import strip_tags

from rest_framework.decorators import api_view
from rest_framework.response import Response

from contact.models import Subscriber

# Create your views here.
def ContactView(request):
   context = {}
   template_name = 'contact/contact-page.html'
   return render(request, template_name, context)


@api_view(['POST'])
def newsletterSubscribe(request):
   if request.method == 'POST':
      data = request.data

      try:
         Subscriber.objects.create(email=str(data))
         send_mail(
            subject='Conkaras Uganda Newsletter',
            message='Thank you for subscribing to our newsletter',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[str(data)]
         )

         return Response('Success')
      except Exception as e:
         print(f'Exception: {e}')
         if str(e).__contains__('UNIQUE'):
            return Response('Already subscribed')
         return Response('Failed, try again later')


@api_view(['POST'])
def sendMessage(request):
   if request.method == 'POST':
      data = request.data
      print(data)
      # message = f"Name: {data.get('name')}\nEmail: {data.get('email')}\nPhone: {data.get('phone')}\nMessage: {data.get('message')}"      
      html_message = render_to_string('contact/components/mail_template.html', {'name': data.get('name'), 'email': data.get('email'), 'phone': data.get('phone'), 'message': data.get('message')})
      plain_message = strip_tags(html_message)

      try:
         send_mail(
            subject=f"Message from {data.get('name')}",
            message=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=settings.TO_EMAILS,
            html_message=html_message
         )

         return Response('SUCCESS')
      except Exception as e:
         print(f'Exception: {e}')
         return Response('Failed, try again later')