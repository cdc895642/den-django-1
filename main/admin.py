from django.contrib import admin
from .models import Post

"""
Depends on view table in admin panel.
"""
admin.site.register(Post)





