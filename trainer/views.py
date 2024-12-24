from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden

import trainer.models

# Create your views here.

def category_page(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def trainer_page(request, trainer_id):
    if request.user.groups.filter(name='Trainer').exists():
        if request.method == "GET":
            service_categories = trainer.models.Category.objects.all()

            my_services = trainer.models.Service.objects.filter(trainer=request.user).all()

            return render(request,"trainer.html", {"categories": service_categories, "services": my_services}) # форма з додаванням сервісу
        return HttpResponse("Hello, world. You're at the polls index.")
    else:
        trainer_model = User.objects.get(id=trainer_id)
        trainer_data = trainer.models.TrainerDescription.objects.filter(trainer=trainer_model)
        trainer_schedule = trainer.models.TrainerSchedule.objects.filter(trainer=trainer_model)

        return render(request, 'account.html', context={'trainer_data': trainer_data, "trainer_schedule": trainer_schedule})

def trainer_service_page(request, user_id, service_id):
    return HttpResponse("Hello, world. You're at the polls index.")

def service_page(request):
    if request.method == "GET":
        services=trainer.Service.objects.all()
        return render(request, "services.html", context={"services":services})
    else:
        if request.user.groups.filter(name='Trainer').exists():
            form_data = request.POST
            service_cat = trainer.models.Category.objects.get(pk=form_data["category"])
            service = trainer.models.Service(
                level = form_data["level"],
                duration = form_data["duration"],
                price = form_data["price"],
                category = service_cat,
                trainer = request.user,
            )
            service.save()
            return redirect("/trainer/")
        else:
            raise HttpResponseForbidden()

def booking_for_user(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def trainer_registration(request):
    if request.method == "GET":
        return render(request, "trainer_signup.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
        trainer_group = Group.objects.get(name="Trainer")
        user.groups.add(trainer_group)
        user.save()
        return HttpResponse("Hello, world. You're at the polls index.")