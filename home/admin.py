from django.contrib import admin

from .models import *

admin.site.register(People)
admin.site.register(Subject)
admin.site.register(Course)