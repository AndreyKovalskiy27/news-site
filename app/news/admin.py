from django.contrib import admin
from news import models


# Register your models here.
admin.site.register(models.Information)


@admin.register(models.Categories)
class CategoriesAdmin(admin.ModelAdmin):
    """Налаштування категорій для адміна"""
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.News)
class CategoriesAdmin(admin.ModelAdmin):
    """Налаштування категорій для адміна"""
    prepopulated_fields = {"slug": ("title",)}
