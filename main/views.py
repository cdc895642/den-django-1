
from django.views.generic import (
    ListView,
    DetailView,
    CreateView)
from .models import Post,Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from .forms import Creating,AppImg,DocumentForm
from django.shortcuts import render, redirect
import sqlite3
from django.http import HttpResponseRedirect






def HomePage(request):
    News=Post.objects.all()
    Top=Post.objects.order_by('-download')[:5]


    data={'news':News,
          'top':Top,
          'title':'Главная страница'}
    return render(request,'main/homepage.html',data)

class NewsDetailView(DetailView):
    model=Post
    template_name = 'main/news-detail.html'
    context_object_name = 'post'
    def get_context_data(self, **kwards):
        ctx=super(NewsDetailView,self).get_context_data(**kwards)
        ctx['title']=Post.objects.filter(pk=self.kwargs['pk']).first()
        return ctx



    def example(self):
        con = sqlite3.connect('C:\\Users\\cdc89\\Desktop\\Macbook\\mysite\\db.sqlite3')
        cur = con.cursor()
        cur.execute('SELECT file FROM main_post ')
        column = cur.fetchall()
        for file in column:
            file = file
        file['download']=file
        return file

        cur.close()
        con.close()




class CreateNewsView(LoginRequiredMixin,CreateView):

    login_url = '/user/'
    redirect_field_name = 'redirect_to'
    model = Post
    fields = ['title','text','category','img','file']



def category_game(request):
    Category=Post.objects.filter(category__exact='Games')
    data={'example':Category}
    return render(request,'main/category.html',data)
def category_multi(request):
    Category1=Post.objects.filter(category__exact='Multimedia')
    data={'example':Category1}
    return render(request,'main/category.html',data)
def down(request,pk):
    con = sqlite3.connect('C:\\Users\\cdc89\\Desktop\\Macbook\\mysite\\db.sqlite3')
    cur = con.cursor()
    cur.execute('SELECT file FROM main_post ')
    column = cur.fetchone()
    Count=Post.objects.get(pk=pk)
    Count.download +=1
    Count.save()
    cur.close()
    con.close()

    return redirect('users_files/default_DaSqWvJ.zip')






