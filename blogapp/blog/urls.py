from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path("create/",views.create_blog,name="create_blog"),
    path("blog/<int:id>",views.blog_detail,name="blog_detail"),
    path("update/<int:id/",views.update_blog,name="update_blog"),
]