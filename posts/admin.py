from django.contrib import admin
from accounts.admin import user_admin
from posts.models import Post
# Register your models here.

user_admin.register(Post)