from django.shortcuts import redirect, render
from django.conf import settings
from django.core.mail import send_mail

from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.urls.base import reverse_lazy
from django.views import View

from rest_framework.decorators import api_view
from rest_framework.response import Response

from contact.models import Receipient, Subscriber

# Create your views here.
class ContactView(View):
    def get(self, request):
        context = {}
        template_name = 'contact/contact-page.html'
        return render(request, template_name, context)
    
    def post(self, request):
        data = request.POST
        subject = 'Contact Form'
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        response = sendMessage(subject, name, email, message)
        print(response)
        return redirect(reverse_lazy('contact:main-page'))


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


def sendMessage(subject, name, email, message):
    html_message = render_to_string('contact/lib/mail_template.html', {'name': name, 'email': email, 'message': message})

    try:
        send_mail(
        subject=subject,
        message='message',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[receipient for receipient in Receipient.objects.all()],
        html_message=html_message
        )

        return 'SUCCESS'
    except Exception as e:
        print(f'Exception: {e}')
        return 'Failed, try again later'