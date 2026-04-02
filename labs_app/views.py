from django.shortcuts import render
from .models import Topic, Category  # Додаємо імпорт моделей

def home(request):
    # Отримуємо всі теми та категорії для головної сторінки
    topics = Topic.objects.all()
    cats = Category.objects.all()
    return render(request, 'labs_app/index.html', {
        'title': 'Головна сторінка',
        'topics': topics,
        'categories': cats,  # Передаємо категорії для меню
        'page': 'home'
    })

def other(request):
    # Ця функція виправить AttributeError (image_21592e.png)
    cats = Category.objects.all()
    return render(request, 'labs_app/index.html', {
        'title': 'Інша сторінка',
        'categories': cats,
        'page': 'other'
    })