from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("booking/", views.booking, name="booking"),
    path("success/", views.success, name="success"),
    path("bookings/", views.booking_list, name="booking_list"),
    path("complete/<int:booking_id>/", views.complete_booking, name="complete_booking"),
    path("cancel/<int:booking_id>/", views.cancel_booking, name="cancel_booking"),
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),

    # NEW PAGE
    path("available-cabs/", views.available_cabs, name="available_cabs"),
]