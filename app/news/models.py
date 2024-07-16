from os.path import splitext
from datetime import datetime
from django.db import models


def generate_image_filename(instance, filename):
    """Генерує назву зображення"""
    return f"{datetime.now()}_{instance}{splitext(filename)[1]}"


# Create your models here.
class Categories(models.Model):
    """Категорії"""

    name = models.CharField(verbose_name="Назва", max_length=200, unique=True)
    slug = models.SlugField(verbose_name="URL", unique=True)

    class Meta:
        db_table = "categories"
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self) -> str:
        return self.name


class News(models.Model):
    """Новини"""

    image = models.ImageField(
        verbose_name="Зображення",
        upload_to=generate_image_filename,
        blank=True,
        null=True,
    )
    title = models.CharField(verbose_name="Назва", max_length=200, unique=True)
    text = models.TextField(verbose_name="Текст")
    slug = models.SlugField(verbose_name="URL", unique=True)
    category = models.ForeignKey(
        to=Categories, on_delete=models.PROTECT, blank=True, null=True
    )

    class Meta:
        db_table = "news"
        verbose_name = "Новина"
        verbose_name_plural = "Новини"

    def __str__(self) -> str:
        return self.title


class Information(models.Model):
    """Інформація"""

    name = models.CharField(verbose_name="Назва", max_length=200, unique=True)
    value = models.CharField(verbose_name="Значення", max_length=200)

    class Meta:
        db_table = "information"
        verbose_name = "Інформація"
        verbose_name_plural = "Інформація"

    def display(self) -> str:
        """Відобразити у форматі <назва>: <значення>"""
        return f"{self.name}: {self.value}"

    def __str__(self) -> str:
        return self.display()
