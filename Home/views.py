from django.shortcuts import render
from Home.models import Store_Data
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password

def index(request):
    return render(request, 'base.html')

def verify(request):
    if request.method == 'POST':
        name = request.POST.get("Username").strip()
        password = request.POST.get("password")

        try:
            user_instance = Store_Data.objects.get(name=name)

            if check_password(password, user_instance.password):
                messages.success(request, "Login successful!")
                return render(request, 'Hello.html')
            else:
                messages.error(request, "Invalid credentials. Please try again.")

        except Store_Data.DoesNotExist:
            messages.error(request, "User does not exist. Please try again.")
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get("Username")
        password = request.POST.get("password")

        hashed_password = make_password(password)
        try:
            new_user = Store_Data(name = username, password = hashed_password)
            new_user.save()

            messages.success(request, "Your Account has been Registered!")
            return render(request, 'login.html')
        except:
            messages.error(request, "An error occurred while registering your account. Please try again.")
    return render(request, 'register.html')