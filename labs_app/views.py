from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from .models import Topic, Category, PythonLibrary, CartItem, Newsletter, Rating
from .forms import RatingForm


# --- ГОЛОВНІ СТОРІНКИ ---

def home(request):
    topics = Topic.objects.all()
    categories = Category.objects.all()
    return render(request, 'labs_app/index.html', {'topics': topics, 'categories': categories})


def category_page(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    topics = Topic.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'labs_app/category_page.html', {
        'category': category,
        'topics': topics,
        'categories': categories
    })


def other(request):
    libraries = PythonLibrary.objects.all()
    categories = Category.objects.all()
    return render(request, 'labs_app/other.html', {'libraries': libraries, 'categories': categories})


# --- СТОРІНКА ТОВАРУ (З РЕЙТИНГОМ) ---

def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    categories = Category.objects.all()

    # Рахуємо середній бал
    avg_rating = topic.ratings.aggregate(Avg('score'))['score__avg'] or 0

    # Обробка форми оцінки
    if request.method == 'POST' and 'submit_rating' in request.POST:
        rating_form = RatingForm(request.POST)
        if rating_form.is_valid():
            new_rating = rating_form.save(commit=False)
            new_rating.topic = topic
            new_rating.save()
            return redirect('topic_detail', topic_id=topic.id)
    else:
        rating_form = RatingForm()

    return render(request, 'labs_app/topic_detail.html', {
        'topic': topic,
        'categories': categories,
        'avg_rating': round(avg_rating, 1),
        'rating_form': rating_form
    })


# --- КОШИК ---

def add_to_cart(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    # Використовуємо сесію браузера, щоб ідентифікувати користувача
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key

    cart_item, created = CartItem.objects.get_or_create(session_key=session_key, topic=topic)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_detail')


def cart_detail(request):
    if not request.session.session_key:
        request.session.create()
    session_key = request.session.session_key

    cart_items = CartItem.objects.filter(session_key=session_key)
    total_price = sum(item.topic.price * item.quantity for item in cart_items)
    categories = Category.objects.all()

    return render(request, 'labs_app/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'categories': categories
    })


# --- РОЗСИЛКА ---

def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            Newsletter.objects.get_or_create(email=email)
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def decrease_cart_item(request, topic_id):
    session_key = request.session.session_key
    if session_key:
        cart_item = CartItem.objects.filter(session_key=session_key, topic_id=topic_id).first()
        if cart_item:
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete() # Якщо залишилась 1 шт, просто видаляємо товар
    return redirect('cart_detail')