from django.contrib import admin
from .models import Todo
# Register your models here.
#Once a model is registered, it becomes accessible
#  through the admin panel, and you can
#  perform CRUD operations (Create, Read, Update, Delete) on it.
admin.site.register(Todo)