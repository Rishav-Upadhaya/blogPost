from django.shortcuts import render,get_object_or_404
from .models import Blog, User
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from users.models import userForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required



# Create your views here.
def bloghome(request):
    return render(request, "blogs/index.html", {
        # "head": [blog.head for blog in Blog.objects.all()], 
        "head":  Blog.objects.all(),
    })

def post(request, t):
    brief = Blog.objects.get(head = t)
    return render(request, "blogs/post.html",{
        "brief": brief
    })

def author(request, writer):
    try:
        user = User.objects.get(username=writer)
        briefs = Blog.objects.filter(author=user)
        posts = [brief.head for brief in briefs]
    except User.DoesNotExist:
        print("User Donot Exist")
        briefs = []
        posts = []
    
    return render(request, "blogs/author.html", {
        "posts": posts, 
        "briefs": briefs,
         "writer": writer
    })

def createpost(request):
    if User.is_authenticated :
        user = User.objects.all()
        if request.method == "POST":
            title = request.POST["title"]
            description1 = request.POST["description"]
            postimage1 = request.FILES["postimage"]
            if title and description1:
                # Save the blog post
                Blog.objects.create(
                    head=title,
                    description=description1,
                    author=request.user,  # Make sure the user is logged in
                    blog_image = postimage1,
                )
                return HttpResponseRedirect(reverse('bloghome'))
            else:
                return render(request, "blogs/create_blogs.html",{
                    'message': 'Error: Missing title or description.'
                })
        else:
            return render(request, "blogs/create_blogs.html")
    else:
        return render(request, "users/login.html")

def delete_user(request):
    if request.method == "POST":
        post_id = request.POST.get("brief_id")  # Match the form field name
        post = get_object_or_404(Blog, pk=post_id)  # Handle invalid IDs
        if request.user.is_superuser or request.user == post.author:  # Check if the user is the author or admin
            post.delete()
            return HttpResponseRedirect(reverse('bloghome'))
        else:
            return HttpResponseForbidden("You are not authorized to delete this post.")
    

