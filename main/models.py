from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    class Meta():
        db_table = 'category'
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=150, unique=True, verbose_name='Категория',null=True)
    slug = models.SlugField( null=True,blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    CATEGORY={('Games','games'),
              ('Multimedia','multimedia')}
    title = models.CharField(max_length=120)
    text = models.TextField(blank=True,null=True)
    category=models.CharField(max_length=20,choices=CATEGORY,blank=True,null=True)
    img = models.ImageField( upload_to='users_img/%Y/%m/%d',blank=True,null=True,default='default.png')
    file=models.FileField(upload_to='users_files/',blank=True,null=True)
    download=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})



class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.DO_NOTHING  )
    img=models.ImageField(default='default.jpg',upload_to='user_images')

    def __str__(self):
        return f'Профайл пользователя {self.user.username}'









