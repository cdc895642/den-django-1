from django.shortcuts import render, redirect
from .forms import UserOurRegistration
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method =='POST':
        form=UserOurRegistration(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Пользователь {username} был успешно создан!Введите имя и пароль для авторизации.')
            return redirect('user')
    else:
        form = UserOurRegistration()
    return render(request, 'users/registration.html',{'form':form,'title':'Регистрация пользователя'})


@login_required()
def profile(request):
    return render(request,'users/profile.html')