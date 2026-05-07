from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    path('category/<int:category_id>/', views.category_page, name='category_page'),
    path('other/', views.other, name='other'),
    path('add-to-cart/<int:topic_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('subscribe/', views.subscribe_newsletter, name='subscribe_newsletter'),
    path('decrease-cart/<int:topic_id>/', views.decrease_cart_item, name='decrease_cart_item'),
]

