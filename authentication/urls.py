from django.urls import path
from .views import RegisterView, LoginView, VerifyEmail

urlpatterns = [
    path('register', RegisterView.as_view(),name='register'),
    path('login', LoginView.as_view(),name='login'),
    path('verify-email/<uidb64>/<token>', VerifyEmail.as_view(), name='activate'),
]