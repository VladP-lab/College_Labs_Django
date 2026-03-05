from django.contrib import admin
from .models import Category, Topic, PythonLibrary

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')

@admin.register(PythonLibrary)
class PythonLibraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')