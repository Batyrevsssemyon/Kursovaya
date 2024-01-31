from django.urls import path
from . import views
from .views import ProductView

urlpatterns = [
    path('', views.index, name='home'),
    path('check', views.check, name='check'),
    path('response', views.response, name='response'),
    path('api/products/', ProductView.as_view()),
]