from django.contrib import admin
from .models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "head", "description", "author")

admin.site.register(Blog, BlogAdmin)