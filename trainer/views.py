from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def category_page(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def trainer_page(request, user_id):
    return HttpResponse("Hello, world. You're at the polls index.")

def service_page(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def booking_for_user(request):
    return HttpResponse("Hello, world. You're at the polls index.")
