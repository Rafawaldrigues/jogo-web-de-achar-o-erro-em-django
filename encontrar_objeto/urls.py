# encontrat_objeto/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jogo.urls')),  # Inclui as URLs do seu app
]