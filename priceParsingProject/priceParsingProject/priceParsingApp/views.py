from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
#the login_required decorator to protect views
from django.contrib.auth.decorators import login_required
#for class-base views 
from django.contrib.auth.mixins import LoginRequiredMixin
"""Intentionally simple parent class for all views. Only implements
 dispatch-by-method and simple sanity checking."""
#for class-based views
from django.views import View
#import the user class
from django.contrib.auth.models import User
#Register form from the current directory
from .forms import RegisterForm
#Page to enter url of product
from .forms import parseProduct
#To render the list of all products
from .models import listProduct

# Create your views here.

#for now the creation of authentication with 4 pages (protected page is added)

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'account_action/register.html', {'form':form})

def login_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            error_message = "Invalid Credentials!"
    return render(request, 'account_action/login.html', {'error':error_message})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    else:
        return redirect('home')
    #I need to add a html page of logout confirmation 


#home_view
#decotator checking if the user is loged in 
@login_required
def home_view(request):
    return render(request, 'home/home.html')


#view of page for product's url
class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/'
    #'next' to redirect url
    redirect_field_name = 'redirect to'
    
    # def get(self, request):
    #     return render(request, 'after_registration/protected_page.html')
@login_required
def product_url_view(request):
    if request.method == 'POST':
        form = parseProduct(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = parseProduct()
    return render(request, 'after_registration/product_Link.html',{'form':form})

@login_required
def success_view(request):
    lists = listProduct.objects.all()
    return render(request, 'after_registration/success.html', {'lists':lists})



