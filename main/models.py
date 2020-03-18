from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):       #Табличка отвечает за статьи
    CATEGORY={('Games','games'),        #Все категории которые можно выбрать
              ('Multimedia','multimedia')}
    title = models.CharField(max_length=120)        #Название
    text = models.TextField(blank=True,null=True)       #Текст
    category=models.CharField(max_length=20,choices=CATEGORY,blank=True,null=True)      #Категории
    img = models.ImageField( upload_to='users_img/%Y/%m/%d',blank=True,null=True,default='default.png')     #Картинка
    file=models.FileField(upload_to='users_files/',blank=True,null=True)        #Файл
    download=models.PositiveIntegerField(default=0)     #Счетчик
    is_active = models.BooleanField(default=True, verbose_name='Модерация')     #Модерация

    """
    Сама табличка не передает нам название статьи.
    Она передает название объекта(Например,'Post_object 5').
    Следуйщая функция решает эту проблему,
    забираю из таблчики строковое значения поля "title".
    """
    def __str__(self):
        return self.title

    def get_absolute_url(self):     #Отвечает за то,что бы после создания статьи,нас перекидывало на саму статью.
        return reverse('news-detail', kwargs={'pk': self.pk})












