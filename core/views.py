from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if user.is_staff:
                return redirect('admin:index')

            elif user.groups.filter(name='Mchungaji').exists():
                return redirect('mchungaji_home')

            elif user.groups.filter(name='Wahazini').exists():
                return redirect('mhazini_home')

            elif user.groups.filter(name = 'Uwakili').exists():
                return redirect('Uwakili')

            elif user.groups.filter(name = 'Mashemasi').exists():
                return redirect('Mashemasi_home')
            else:
                return redirect('login')
    return render(request, 'core/login.html')



def register(request):
    if request.method == 'POST':
        jina = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
           messages.error(request, 'Password do not Match')
           return redirect('register')

        if User.objects.filter(username=jina).exists():
            messages.error(request,'username exists')
            return redirect('register')

        user = User.objects.create_user(
            username = jina,
            email = email,
            password=password1
        ).user.save()
        messages.success(request,'Account is successfully created')
        return redirect('login')

    return render (request,'core/register.html')

@login_required
def dashboard(request):
    return render(request,'dashboard,html')
