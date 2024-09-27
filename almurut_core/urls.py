"""
URL configuration for almurut_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from market.views import HomeView, ProductListView, ProductDetailView, SendProductFeedbackView
from users.views import UserRegistrationView, LoginPageView, UserMakeLoginView, UserMakeLogoutView, \
    UserMakeRegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
    path('product-detail/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product-detail/<int:pk>/send-feedback/', SendProductFeedbackView.as_view(), name='send-feedback-url'),
    path('registration/', UserRegistrationView.as_view(), name='registration-url'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('make-login/', UserMakeLoginView.as_view(), name='make-login-url'),
    path('make-logout', UserMakeLogoutView.as_view(), name='make-logout-url'),
    path('make-registration/', UserMakeRegistrationView.as_view(), name='make-registration-url')
]







urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)