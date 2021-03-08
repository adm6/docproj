from django.contrib import admin
from .models import Article, Marathon, Reception, Consultation


# Register your models here.
admin.site.register(Article)
admin.site.register(Marathon)
admin.site.register(Reception)
admin.site.register(Consultation)