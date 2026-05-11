import uuid
import os

from django.db import models
from django.core.validators import FileExtensionValidator # Валидация типов файлов для изображений


# Функции для генерации уникальных имен файлов (перед моделями)
def news_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('news_images', filename)

def vacancy_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('vacancies_images', filename)

# Таблицы
class News(models.Model):

    class Meta:
        ordering = ['-publish_date']         # Сортировка по умолчанию
        verbose_name = 'Новость'             # Человеко-читаемое имя в единственном числе
        verbose_name_plural = 'Новости'      # Человеко-читаемое имя во множественном числе

    news_id = models.AutoField(primary_key=True)        # INTEGER, PK
    title = models.CharField(max_length=255)            # VARCHAR(255)
    content = models.TextField()                        # VARCHAR(max)
    publish_date = models.DateTimeField(db_index=True)               # DATETIME
    is_published = models.BooleanField(default=False, db_index=True)   # BOOLEAN
    image = models.ImageField(
        upload_to=news_image_path, 
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp']),], 
        blank=True, 
        null=True
    )

    def __str__(self):
        return self.title # Вывод для дебага


class Vacancies(models.Model):

    class Meta:
        ordering = ['-publish_date']        # Сортировка по умолчанию
        verbose_name = 'Вакансия'           # Человеко-читаемое имя в единственном числе
        verbose_name_plural = 'Вакансии'    # Человеко-читаемое имя во множественном числе

    vacancy_id = models.AutoField(primary_key=True)     # INTEGER, PK
    title = models.CharField(max_length=255)            # VARCHAR(255)
    salary = models.CharField(max_length=100)           # VARCHAR(100)
    description = models.TextField()                    # VARCHAR(max)
    publish_date = models.DateTimeField(db_index=True)               # DATETIME
    is_published = models.BooleanField(default=False, db_index=True)   # BOOLEAN
    image = models.ImageField(
        upload_to=vacancy_image_path, 
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp']),], 
        blank=True, 
        null=True
    )

    def __str__(self):
        return f"{self.title} - {self.salary}" # Вывод для дебага