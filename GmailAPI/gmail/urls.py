from django.urls import path

from . import views

urlpatterns = [
    path('', views.RequestView.as_view(), name='request'),
    path('result/', views.ResultView.as_view(), name='result')
]
