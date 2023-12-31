from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from posts.models import Post

from products.models import Category

# Create your views here.

class IndexView(View):
    def get(self, request):
        template_name = "main/index.html"
        posts = Post.objects.all().order_by('date_modified')[:3]
        context = {
            'categories': Category.objects.all(),
            'posts': posts,
        }
        return render(request, template_name, context)

class AboutView(View):
    def get(self, request):
        template_name = "main/about.html"
        context = {}
        return render(request, template_name, context)  

class TermsAndPrivacyView(View):
    def get(self, request):
        template_name = "main/terms-privacy.html"
        context = {}
        return render(request, template_name, context) 


class MicroLoanView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'main/microloans.html'
        context = {}
        return render(request, template_name, context) 

