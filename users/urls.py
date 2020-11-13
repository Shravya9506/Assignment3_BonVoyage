from . import views
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import url


app_name = 'users'

urlpatterns = [
    re_path(r'register_customer/', views.register_customer, name='register_customer'),
    re_path(r'edit_profile/', views.edit_customer, name='edit_customer'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('users/password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('password_reset_form/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset_form'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('mark_as_favorite/<int:pk>', views.mark_as_favorite, name='mark_as_favorite'),
    path('unmark_as_favorite/<int:pk>', views.unmark_as_favorite, name='unmark_as_favorite'),
]
