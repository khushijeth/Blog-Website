from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name="home"),
    path("create/",views.create_blog,name="create_blog"),
    path("blog/<int:id>",views.blog_detail,name="blog_detail"),
    path("update/<int:id>/",views.update_blog,name="update_blog"),
    path("delete/<int:id>",views.delete_blog,name="delete_blog"),
    path("register/",views.register,name="register"),
    path("login/",auth_views.LoginView.as_view(template_name="registration/login.html"),name="login"),
    path("logout/",auth_views.LogoutView.as_view(),name="logout"),
]