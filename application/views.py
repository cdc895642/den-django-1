from django.shortcuts import render

def index(request):
    data={
        'title':'Подать заявку'
    }
    return render(request,'application/application.html',data)
