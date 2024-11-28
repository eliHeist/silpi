from django.contrib import admin
from accounts.admin import user_admin
from posts.models import Post
from unfold.admin import ModelAdmin
# Register your models here.

@admin.register(Post)
class PostAdminClass(ModelAdmin):
    pass