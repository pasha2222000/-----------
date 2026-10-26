from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.main, name="main"),
    path('post/<int:id>/', views.test,name='post_detail'),
    path('profile/<int:id>/', views.profile, name='user_page'),
    path("post/new/", views.PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/edit/", views.PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page= 'main'), name= 'logout'),
    path('register/', views.register, name='register')
]


