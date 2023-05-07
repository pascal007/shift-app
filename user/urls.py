from django.urls import path

from user.views import UserRegistrationView, UserLoginView, MyTokenRefreshView

app_name = 'user'

urlpatterns = [
    path("register", UserRegistrationView.as_view()),
    path("login", UserLoginView.as_view()),
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh')
]
