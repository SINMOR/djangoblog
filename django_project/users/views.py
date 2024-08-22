from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get(
                "username"
            )  # gets the username from the databse and stores it as an object
            messages.success(request, f"Account Created for {username} !")
            return redirect("blog-home")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})
