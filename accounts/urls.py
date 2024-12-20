from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView
from django.urls import path

from accounts.views import SignupView


app_name = 'accounts'

# urlpatterns = [
#     path('signup/', SignupView.as_view(), name='signup'),
#     path('login/', LoginView.as_view(), name='login'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
#     path('password-reset-done/', PasswordResetDoneView.as_view(), name='password-reset-done'),
#     path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
#     path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password-reset-complete'),
# ]