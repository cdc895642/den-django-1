from django.contrib import admin
from .models import Post

"""
Отвечает за вывод таблички в админ панеле.
"""
admin.site.register(Post)





