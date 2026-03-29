from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        error = []

        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        
        if User.objects.filter(username=username).exists():
            error.append('username')

        if User.objects.filter(email=email).exists():
            error.append('email')

        if password1 != password2:
            error.append('password')

       
        if not error:
            user = User.objects.create_user(
                username=username,
                first_name=firstname,
                last_name=lastname,
                email=email,
                password=password1
            )
            user.save()
            return redirect('/')

        return render(request, 'register.html', {'error': error})

    return render(request, 'register.html')