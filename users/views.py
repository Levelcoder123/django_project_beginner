from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from users.models import CustomUser


# login view
def login_view(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_password = request.POST.get('password')
        user = authenticate(request, username=user_name, password=user_password)

        if user is not None:
            login(request, user)

            return redirect('/accounts')
        else:
            return render(request, 'login.html', {'error': 'invalid login'})

    else:
        return render(request, 'login.html')


# sign up view
def signup_view(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        user_number = request.POST.get('number')
        user_address = request.POST.get('address')

        CustomUser.objects.create_user(username=user_name, email=user_email,
                                       password=user_password, phone_number=user_number,
                                       address=user_address)
        return redirect('login')
    else:
        return render(request, 'signup.html')
