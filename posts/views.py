from django.shortcuts import render
from django.views import View

from posts.models import Post

# Create your views here.
class PostsView(View):
    def get(self, request):
        posts = Post.objects.all().order_by('date_modified')
        template_name = 'posts/post-list.html'
        context = {
            'posts': posts
        }
        return render(request, template_name, context)

class PostView(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        template_name = 'posts/post-detail.html'
        context = {
            'post': post
        }
        return render(request, template_name, context)
