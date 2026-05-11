from django.contrib import admin
from .models import News, Vacancies


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'is_published')
    list_filter = ('is_published', 'publish_date')
    search_fields = ('title', 'content')
    readonly_fields = ('news_id',)
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'image', 'is_published')
        }),
        ('Дата публикации', {
            'fields': ('publish_date',),
            'classes': ('collapse',)
        }),
    )

@admin.register(Vacancies)
class VacanciesAdmin(admin.ModelAdmin):
    list_display = ('title', 'salary', 'publish_date', 'is_published')
    list_filter = ('is_published', 'publish_date')
    search_fields = ('title', 'description')
    readonly_fields = ('vacancy_id',)