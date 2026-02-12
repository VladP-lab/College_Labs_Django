from django.shortcuts import render

def home(request):
    context = {
        'title': 'Головна сторінка',
        'content': 'Вітаю на головній! Тут є посилання на інші розділи.',
        'page_type': 'home'
    }
    return render(request, 'labs_app/index.html', context)

def other(request):
    context = {
        'title': 'Друга сторінка',
        'content': 'Це контент, переданий через контекст для іншої сторінки!',
        'show_link': False
    }
    return render(request, 'labs_app/index.html', context)