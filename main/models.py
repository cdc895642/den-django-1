from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

#Table depends on all apps
class Post(models.Model):
    #All cetegories which we can choose
    CATEGORY={('Games','games'),
              ('Multimedia','multimedia')}
    title = models.CharField(max_length=120)
    text = models.TextField(blank=True,null=True)
    category=models.CharField(max_length=20,choices=CATEGORY,blank=True,null=True)
    img = models.ImageField( upload_to='users_img',blank=True,null=True,default='default.png')
    file=models.FileField(upload_to='users_files/',blank=True,null=True)
    #Counter
    download=models.PositiveIntegerField(default=0)
    #TODO связано с счетчиком и скачиванием файла.Добавил по примеру,не понимаю как роботает.
    is_active = models.BooleanField(default=True, verbose_name='Модерация')

    """
    Table dont give us name of app(title).
    It returns only name of object(For example,'Post_object 5').
    Next function deal with this problem,
    taking from table string "title".
    """
    def __str__(self):
        return self.title

    #Depends on ,when we add new app,site redirects us to detail view of this app.
    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})












