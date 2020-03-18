from django.views.generic import (
    ListView,
    DetailView,
    CreateView)
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.shortcuts import render, redirect
import sqlite3


def HomePage(request):      #Отвечает за вывод главной страницы
    News=Post.objects.all()     #Собирает все статьи из таблички и выводит их
    Top=Post.objects.order_by('-download')[:5]      #Собирает пять статей и сортирует их по количеству скачиваний

    data={'news':News,
          'top':Top,
          'title':'Главная страница'}
    return render(request,'main/homepage.html',data)


class NewsDetailView(DetailView):       #Детальный просмотор каждой статьи
    model=Post
    template_name = 'main/news-detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwards):       #Отвечаает за вывод названий статьи в тайтле
        ctx=super(NewsDetailView,self).get_context_data(**kwards)
        ctx['title']=Post.objects.filter(pk=self.kwargs['pk']).first()
        return ctx


class CreateNewsView(LoginRequiredMixin,CreateView):        #Отвечает за созадний новой статьи
    login_url = '/user/'
    redirect_field_name = 'redirect_to'
    model = Post
    fields = ['title','text','category','img','file']

"""
Ниже приведенные функции c названием "category_..." отвечают за вывод статей по категориям.
Переменные Category собирают все статьи 
и фильтрует их по названию указанной категории"category__exact".
"""
def category_game(request):
    Category=Post.objects.filter(category__exact='Games')
    data={'example':Category}
    return render(request,'main/category.html',data)
def category_multi(request):
    Category1=Post.objects.filter(category__exact='Multimedia')
    data={'example':Category1}
    return render(request,'main/category.html',data)


def down(request,pk):       #Отвечает за счетчик скачиваний и скачивание файла
    price = Post.objects.get(pk=pk)     #Собирает все статьи и каждой дает свой pk"primary key"
    price.download += 1     #Добавляет +1 к счетчику
    price.save()        #Сохраняет измениния
    return redirect(price.file.url)     #Возравщает ссылку на файл






