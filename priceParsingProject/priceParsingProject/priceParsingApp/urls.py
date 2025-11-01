from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('protected/', views.product_url_view, name='protected'),
    path('', views.home_view, name='home'),
    path('success', views.success_view, name='success'),
]
