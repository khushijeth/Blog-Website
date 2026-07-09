from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from . models import Blog 
from . forms import BlogForm , RegisterForm
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

# Create your views here.
# def home(request):
#     return HttpResponse("Hello User !!")
def home(request):
    blogs=Blog.objects.all().order_by("-created_at")

    context={
        'blogs':blogs
    }
    return render(request,"home.html",context)

@login_required
def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES)
        
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('home')
    else:
        form = BlogForm()

    context = {
        "form":form
    }

    return render(request,"create_blog.html",context)

# @login_required
def blog_detail(request,id):
    blog=get_object_or_404(Blog,id=id)

    return render(request,"blog_detail.html",{"blog":blog})

@login_required
def update_blog(request,id):
    blog=get_object_or_404(Blog,id=id,author=request.user)

    if request.method == "POST":
        form = BlogForm(
            request.POST,
            request.FILES,
            instance=blog
        )
        if form.is_valid():
            form.save()
            return redirect("home")
        
    else:
        form = BlogForm(instance = blog)
    
    return render(request,"create_blog.html",{"form":form})

@login_required
def delete_blog(request,id):
    blog = get_object_or_404(Blog,id=id,author=request.user)
    if request.method == "POST":
        blog.delete()
        return redirect("home")
    
    return render(request,"delete_blog.html",{"blog":blog})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("User Created")
            return redirect("login")
        else:
            print(form.errors)
    else:
        form = RegisterForm()

    return render(request,"registration/register.html",{"form":form})

