from django.shortcuts import render , redirect , get_object_or_404
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

def blog_detail(request,id):
    blog=get_object_or_404(Blog,id=id)
    return render(request,"blog_detail.html",{
        "blog":blog
    })
