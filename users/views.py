from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
<<<<<<< HEAD
from django.contrib.auth.models import User, Group
=======
from django.contrib.auth.models import User
>>>>>>> f3f8c0c9420f13ab02e6dba2204770ae42a343c7
from django.shortcuts import render

# Create your views here.
def user_page(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def specific_user(request, user_id):
    return HttpResponse("Hello, world. You're at the polls index.")

def login_page(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("You're logged in.")
        else:
            return render(request, "login.html")
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponse("logged_out")
    return HttpResponse("login_first")

def register_page(request):
    if request.method == "GET":
        return render(request, "register.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
<<<<<<< HEAD
        client_group = Group.objects.get(name="Client")
        user.groups.add(client_group)
=======
>>>>>>> f3f8c0c9420f13ab02e6dba2204770ae42a343c7
        user.save()
        return HttpResponse("Hello, world. You're at the polls index.")
