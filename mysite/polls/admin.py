from django.contrib import admin

# Register your models here.

# Make the poll app modifiable in the admin
from .models import Question,Choice

admin.site.register(Question)
admin.site.register(Choice)