from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('all-news/', views.all_news, name="all-news"),
    path('detail/<int:id>/', views.detail, name="detail"),
    path('registration/', views.CustomerRegistrationView.as_view(), name="registration")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
