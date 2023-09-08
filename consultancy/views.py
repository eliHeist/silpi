from django.shortcuts import render
from django.views import View

from consultancy.models import ConsultancyProject

# Create your views here.
class IndexView(View):
    def get(self, request):
        template_name = 'consultancy/consultancy.html'
        context = {}
        return render(request, template_name, context)


class ConsultancyListView(View):
    def get(self, request, *args, **kwargs):
        projects = ConsultancyProject.objects.all()
        template_name = 'consultancy/projects.html'
        context = {
            "projects": projects
        }
        return render(request, template_name, context)


