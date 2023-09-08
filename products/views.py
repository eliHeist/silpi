from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
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


class ProductDetailView(DetailView):
    template_name = 'products/product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'


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