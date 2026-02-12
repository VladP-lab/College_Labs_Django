from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('labs_app.urls')), # Це посилає запити в твій додаток
]