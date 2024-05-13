from . import forms
from django.shortcuts import redirect, render


# Create your views here.


def app_quote(request):
    if request.method == "POST":
        form = forms.QuoteForm(
            request.POST,
        )
        if form.is_valid():
            return redirect("home")
    else:
        form = form.QuoteForm()
    return render(request, "appointments/create_quote.html", {"form": form})


def app_vehicle_showing(request):
    if request.method == "POST":
        form = forms.VehicleShowingForm(
            request.POST,
        )
        if form.is_valid():
            return redirect("home")
    else:
        form = forms.VehicleShowingForm()
    return render(request, "appointments/create_showing.html", {"form": form})


def create_appointment(request):
    if request.method == "POST":
        vehicle_showing_form = forms.VehicleShowingForm(request.POST)
        quote_form = forms.QuoteForm(request.POST)
        if vehicle_showing_form.is_valid():
            vehicle_showing_form.save()
            return redirect("home")
        if quote_form.is_valid():
            quote_form.save()
            return redirect("home")
    else:
        vehicle_showing_form = forms.VehicleShowingForm()
        quote_form = forms.QuoteForm()
        print("Quote form errors:", quote_form.errors)
        print("Vehicle showing form errors:", vehicle_showing_form.errors)
    return render(
        request,
        "appointments/appointment_form.html",
        {"vehicle_showing_form": vehicle_showing_form, "quote_form": quote_form},
    )
