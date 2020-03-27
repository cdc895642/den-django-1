from django.views.generic import (
    ListView,
    DetailView,
    CreateView)
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.shortcuts import render, redirect
import sqlite3
from zipfile import ZipFile

from django.http import HttpResponseRedirect
from django.shortcuts import render
import hashlib



#Depends on view homepage
def HomePage(request):
    # Collecting all apps from table Post
    News=Post.objects.all()
    # Collecting 5 apps and sort they by number of downloaded files
    Top=Post.objects.order_by('-download')[:5]

    data={'news':News,
          'top':Top,
          'title':'Главная страница'}
    return render(request,'main/homepage.html',data)

#Detail view of concrete app
class NewsDetailView(DetailView):
    model=Post
    template_name = 'main/news-detail.html'
    context_object_name = 'post'
    #Depends on view name of concrete app in title
    def get_context_data(self, **kwards):
        ctx=super(NewsDetailView,self).get_context_data(**kwards)
        ctx['title']=Post.objects.filter(pk=self.kwargs['pk']).first()
        return ctx

#Depends on creating new app
class CreateNewsView(LoginRequiredMixin,CreateView):
    login_url = '/user/'
    redirect_field_name = 'redirect_to'
    model = Post
    fields = ['title','text','category','file']

    def get_context_data(self, **kwards):
        ctx = super(CreateNewsView, self).get_context_data(**kwards)
        ctx['title'] = 'Создание новой программы'
        return ctx

    def form_valid(self,form):
        instance=form.save()
        #P=Post.objects.get(pk=instance.id)
        zipFile=ZipFile(instance.file, 'r')
        Big = zipFile.extract('big.png')
        Small = zipFile.extract('small.png')
        zipFile.close()

        #Adding photos in database
        instance.BigImg=Big
        instance.SmallImg=Small

        instance.save()

        return super(CreateNewsView, self).form_valid(form)


"""
Undermentioned function with name "category_..." depends on view apps with concrete category.
Variable "Category" collect all apps 
and sort they by concrete category (category__exact).
"""
def category_game(request):
    Category=Post.objects.filter(category__exact='Games')
    data={'example':Category}
    return render(request,'main/category.html',data)
def category_multi(request):
    Category1=Post.objects.filter(category__exact='Multimedia')
    data={'example':Category1}
    return render(request,'main/category.html',data)

#Depends on downloading files and count amount of downloading
def down(request,pk):
    #Collect all apps and every gives their personal pk"primary key"
    price = Post.objects.get(pk=pk)
    # Adds 1 to counter
    price.download += 1
    #Saves changes
    price.save()
    # Redirect us to personal path of path
    return redirect(price.file.url)









