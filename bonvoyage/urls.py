from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from bonvoyage import views

urlpatterns = [
    path('', views.home, name='home'),
    path('message/', views.message, name='message'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)