from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.shortcuts import redirect, render
from django.views import View
from contact.models import Receipient

from vehicles.models import Vehicle, VehicleOrderRequest

# Create your views here.
class VehicleListView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'vehicles/vehicle-list.html'
        vehicles = Vehicle.objects.all()
        context = {
            'vehicles': vehicles,
        }
        return render(request, template_name, context)
    

class VehicleRequestView(View):
    def get(self, request, pk, *args, **kwargs):
        template_name = 'vehicles/vehicle-request.html'
        vehicle = Vehicle.objects.get(pk=pk)
        context = {
            'vehicle': vehicle,
        }
        return render(request, template_name, context)

    def post(self, request, pk, *args, **kwargs):
        data = request.POST
        vehicle = Vehicle.objects.get(pk=pk)
        # TODO create vehicle order object
        order = VehicleOrderRequest(
            vehicle=vehicle,
            name=data.get('name'),
            email=data.get('email'),
            phone=data.get('phone'),
            action=data.get('action')
        )
        order.save()
        
        # TODO send emails
        # Send email to TO_EMAILS
        to_emails_message = render_to_string('vehicles/order-notification.html', {'order':order})
        send_mail(
            'New Order',
            '',
            settings.DEFAULT_FROM_EMAIL,  # Replace with your email
            [r.email for r in Receipient.objects.all()],  # Replace with your recipient emails
            html_message=to_emails_message,
        )

        # Render the user email template
        user_message = render_to_string('vehicles/order-confirmation-user.html', {'email':order.email})

        # Send confirmation email to the user
        send_mail(
            'Order Confirmation',
            '',
            settings.DEFAULT_FROM_EMAIL,  # Replace with your email
            [order.email],
            html_message=user_message,
            fail_silently=False,
        )
        return self.get(request, pk=pk)


