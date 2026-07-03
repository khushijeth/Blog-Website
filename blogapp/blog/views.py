from django.shortcuts import render , redirect
from django.http import HttpResponse
from . models import Blog 
from . forms import BlogForm

# Create your views here.
# def home(request):
#     return HttpResponse("Hello User !!")
def home(request):
    blogs=Blog.objects.all().order_by("-created_at")

    context={
        'blogs':blogs
    }
    return render(request,"home.html",context)

def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST,request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForm()

    context = {
        "form":form
    }

    return render(request,"create_blog.html",context)