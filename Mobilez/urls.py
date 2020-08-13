from django.contrib import admin
from django.urls import path, include
from allauth.account.views import LoginView, ConfirmEmailView
from allauth.account import views as allauth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name="login"),
    path('confirmEmail/', ConfirmEmailView.as_view(), name="account_confirm_email"),
    path('', include('allauth.urls')),
    path('', allauth_views.login, name="account_login"),
    path('accueil/', include('accueil.urls')),
    path('map/', include('map.urls')),
]
