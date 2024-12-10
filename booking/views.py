from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def booking_page(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def booking_cancel(request, user_id):
    return HttpResponse("Hello, world. You're at the polls index.")

def booking_acception(request):
    return HttpResponse("Hello, world. You're at the polls index.")