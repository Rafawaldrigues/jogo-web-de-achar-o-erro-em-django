# jogo/apps.py
from django.apps import AppConfig

class JogoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jogo'  # <-- Isso deve estar exatamente assim