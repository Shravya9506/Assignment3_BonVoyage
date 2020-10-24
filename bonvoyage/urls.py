from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from bonvoyage import views

urlpatterns = [
    path('bonvoyage/home/', views.home, name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)