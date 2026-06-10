from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tymy/', views.seznam_tymu, name='seznam_tymu'),
    path('tymy/<int:tym_id>/', views.detail_tymu, name='detail_tymu'),
    path('zapasu/', views.seznam_zapasu, name='seznam_zapasu'),
]