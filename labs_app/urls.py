from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),        # Це твоя головна (вже працює)
    path('other/', views.other, name='other'), # ДОДАЙ ЦЕЙ РЯДОК
]