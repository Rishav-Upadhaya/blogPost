from django.contrib import admin
from .models import Blog, Useractivity

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "head", "author")

class Useractivityadmin(admin.ModelAdmin):
    list_display = ("usernameid", "postid", "commentdes", "commented_at")


admin.site.register(Blog, BlogAdmin)
admin.site.register(Useractivity, Useractivityadmin)