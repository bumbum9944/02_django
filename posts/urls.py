from django.urls import path
from . import views

urlpatterns = [
    # 아래 각 주소 앞에는 post/가 생략되어 있다. ''로 놓으면 post/만 있는것
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
]
