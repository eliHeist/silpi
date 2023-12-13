from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from contact.models import Receipient
from products.forms import ProductModelForm

from products.models import Category, Product


# Create your views here.
class CategoryListView(ListView):
    template_name = 'products/landing.html'
    queryset = Category.objects.all()
    context_object_name = 'categories'


class ProductListView(View):
    def get(self, request, pk=None):
        template_name = 'products/product_list.html'
        
        if pk:
            category = Category.objects.get(pk=pk)
            products = category.products.filter(available=True)
        else:
            category = 'All Products'
            products = Product.objects.filter(available=True)
        context = {
            'category': category,
            'products': products,
        }
        return render(request, template_name, context)


class ProductDetailView(View):
    def get(self, request, pk):
        template_name = 'products/product_detail.html'
        
        product = Product.objects.get(pk=pk)
        context = {
            'product': product,
        }
        return render(request, template_name, context)
    
    def post(self, request, pk):
        class Order():
            def __init__(self,product,name,email,phone) -> None:
                self.product = product
                self.name = name
                self.email = email
                self.phone = phone
                
        product = Product.objects.get(pk=pk)
        data = request.POST
        order = Order(product,data.get('name'),data.get('email'),data.get('phone'))
        
        # TODO send emails
        # Send email to TO_EMAILS
        to_emails_message = render_to_string('products/order-notification.html', {'order':order})
        send_mail(
            'Product Quotation Request',
            '',
            settings.DEFAULT_FROM_EMAIL,  # Replace with your email
            [r.email for r in Receipient.objects.all()],  # Replace with your recipient emails
            html_message=to_emails_message,
        )

        # Render the user email template
        user_message = render_to_string('vehicles/order-confirmation-user.html', {'email':data.get('email')})

        # Send confirmation email to the user
        send_mail(
            'Quotation Confirmation',
            '',
            settings.DEFAULT_FROM_EMAIL,  # Replace with your email
            [order.email],
            html_message=user_message,
            fail_silently=False,
        )
        return self.get(request, pk=pk)


class ProductCreateView(LoginRequiredMixin, CreateView):
    template_name = 'products/product_create.html'
    form_class = ProductModelForm


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'products/product_update.html'
    queryset = Product.objects.all()
    form_class = ProductModelForm

    def get_success_url(self):
        return reverse('products:productspage')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'products/product_delete.html'
    queryset = Product.objects.all()
    form_class = ProductModelForm

    def get_success_url(self):
        return reverse('products:productspage')