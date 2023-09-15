from django.shortcuts import redirect, render
from django.conf import settings
from django.core.mail import send_mail

from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views import View

from rest_framework.decorators import api_view
from rest_framework.response import Response

from contact.models import Subscriber

# Create your views here.
class ContactView(View):
    def get(self, request):
        print(f'\nGET\n{request.GET}\n\n')
        context = {}
        template_name = 'contact/contact-page.html'
        return render(request, template_name, context)
    
    def post(self, request):
        print(f'\nPOST\n{request.POST}\n\n')
        sendMessage(request.POST)
        return redirect('contact:main-page')


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


def sendMessage(data):
    html_message = render_to_string('contact/components/mail_template.html', {'name': data.get('name'), 'email': data.get('email'), 'message': data.get('message')})

    try:
        send_mail(
        subject=f"Message from {data.get('name')}",
        message='',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=settings.TO_EMAILS,
        html_message=html_message
        )

        return Response('SUCCESS')
    except Exception as e:
        print(f'Exception: {e}')
        return Response('Failed, try again later')