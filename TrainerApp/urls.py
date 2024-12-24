"""
URL configuration for TrainerApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import users.views
import trainer.views
import booking.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/", include("users.urls")),
    path("login/", users.views.login_page, name="user_login"),
    path("logout/", users.views.logout_page, name="user_logout"),
    path("register/", users.views.register_page, name="user_register"),
<<<<<<< HEAD
    path("register/trainer/", trainer.views.trainer_registration, name="trainer_registration"),
=======
>>>>>>> f3f8c0c9420f13ab02e6dba2204770ae42a343c7
    path("trainer/", include("trainer.urls")),
    path("category/", trainer.views.category_page, name="trainer_category"),
    path("service/", trainer.views.service_page, name="trainer_service"),
    path("userbook/", trainer.views.booking_for_user, name="booking_for_user"),
    path("booking/", include("booking.urls")),
    path("cancel/", booking.views.booking_cancel, name="booking_cancel"),
    path("acception/", booking.views.booking_acception, name="booking_acception"),

]
