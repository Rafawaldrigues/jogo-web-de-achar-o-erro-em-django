from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),  # Esta linha deve existir
    path('phase/<int:phase_number>/', views.phase, name='phase'),
    path('check_answer/', views.check_answer, name='check_answer'),
    path('congratulations/', views.congratulations, name='congratulations'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)