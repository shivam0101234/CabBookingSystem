from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking, Cab
import random
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")

@login_required
def booking(request):

    if request.method == "POST":

        cab_type = request.POST["cab_type"]

        available_cabs = Cab.objects.filter(
            cab_type=cab_type,
            is_available=True
        )

        if not available_cabs.exists():
            return render(request, "booking.html", {
                "error": "No cab available in this category."
            })

        assigned_cab = random.choice(list(available_cabs))

        Booking.objects.create(
            name=request.POST["name"],
            mobile=request.POST["mobile"],
            pickup=request.POST["pickup"],
            drop=request.POST["drop"],
            members=request.POST["members"],
            cab_type=cab_type,
            assigned_cab=assigned_cab.cab_name,
            driver_name=assigned_cab.driver_name,
            car_number=assigned_cab.car_number,
            date=request.POST["date"],
            time=request.POST["time"],
        )

        assigned_cab.is_available = False
        assigned_cab.save()

        return redirect("/success/")

    return render(request, "booking.html")


def success(request):
    booking = Booking.objects.latest("id")

    return render(request, "success.html", {
        "booking": booking
    })
@login_required
def booking_list(request):

    search = request.GET.get("search")

    if search:
        bookings = Booking.objects.filter(name__icontains=search) | Booking.objects.filter(mobile__icontains=search)
    else:
        bookings = Booking.objects.all()

    return render(request, "booking_list.html", {
        "bookings": bookings,
        "search": search
    })
@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if booking.status != "Cancelled":

        booking.status = "Cancelled"
        booking.save()

        cab = Cab.objects.filter(
            car_number=booking.car_number
        ).first()

        if cab:
            cab.is_available = True
            cab.save()

    return redirect("/bookings/")
@login_required
def complete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if booking.status != "Completed":
        booking.status = "Completed"
        booking.save()

        cab = Cab.objects.filter(
            car_number=booking.car_number
        ).first()

        if cab:
            cab.is_available = True
            cab.save()

    return redirect("/bookings/")

@login_required
def available_cabs(request):
    cabs = Cab.objects.filter(is_available=True)
    return render(request, "available_cabs.html", {"cabs": cabs})
def register(request):

    if request.method == "POST":

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("/register/")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Registration Successful")
        return redirect("/login/")

    return render(request, "register.html")


def login_user(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)
            return redirect("/")

        else:

            messages.error(request, "Invalid Username or Password")

    return render(request, "login.html")


def logout_user(request):

    logout(request)
    return redirect("/login/")