from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

from django.views import View
from django.views.generic import FormView, TemplateView
from django.urls.base import reverse
from django.shortcuts import get_object_or_404, render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from cart.forms import CheckoutForm

from products.models import Product
from .models import CartItem, Order, OrderItem
from .serializers import CartItemSerializer

class AddToCartView(APIView):
    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data['product_id']
            quantity = serializer.validated_data['quantity']
            session_key = request.session.session_key

            # Check if the item is already in the cart for this session
            cart_item, created = CartItem.objects.get_or_create(
                session_key=session_key,
                product_id=product_id,
            )

            if not created:
                cart_item.quantity += quantity  # Update the quantity if item exists
            else:
                cart_item.product = get_object_or_404(Product, id=product_id)

            cart_item.save()

            return Response({'message': 'Item added/updated in cart successfully.'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CartView(View):
    def get(self, request):
        session_key = request.session.session_key
        items = CartItem.objects.filter(session_key=session_key)
        cart_items = []
        for item in items:
            it = {
                "id": item.pk,
                "pdt_pk": item.product.pk,
                "quantity": item.quantity,
                "price": item.product.price,
                "name": item.product.name,
                "image": item.product.thumbnail.url,
            }
            cart_items.append(it)
        
        context = {
            'cart_items': cart_items
        }
        return render(request, 'cart/cart.html', context)

class CheckoutAPIView(APIView):
    def post(self, request):
        # Extract data from the request
        email = request.data.get('email')
        phone = request.data.get('phone')
        items = request.data.get('items')

        # Create a new Order object
        order = Order(email=email, phone=phone)
        order.save()

        # Iterate through the items and create OrderItems objects
        for item_data in items:
            product_id = item_data.get('pdt_pk')
            quantity = item_data.get('quantity')

            # Get the product from your Product model (replace Product with your actual model)
            product = Product.objects.get(pk=product_id)

            # Create an OrderItems object and associate it with the Order
            order_item = OrderItem(product=product, quantity=quantity, order=order)
            order_item.save()

        email_data = {
            'user_email': email,
            'user_phone': phone,
            'items': items,
        }

        # Send email to TO_EMAILS
        to_emails_message = render_to_string('cart/order-notification.html', email_data)
        send_mail(
            'New Order',
            '',
            settings.DEFAULT_FROM_EMAIL,  # Replace with your email
            settings.TO_EMAILS,  # Replace with your recipient emails
            html_message=to_emails_message,
        )

        # Render the user email template
        user_message = render_to_string('cart/order-confirmation-user.html', email_data)

        # Send confirmation email to the user
        send_mail(
            'Order Confirmation',
            '',
            settings.DEFAULT_FROM_EMAIL,  # Replace with your email
            [request.data['email']],
            html_message=user_message,
            fail_silently=False,
        )

        if session_key := request.session.session_key:
            CartItem.objects.filter(session_key=session_key).delete()

        # Your checkout response logic here...

        return Response({'message': 'Order placed successfully.', "done": True, "url": str(reverse('cart:success')) })

class SuccessView(TemplateView):
    template_name = 'cart/success.html'

