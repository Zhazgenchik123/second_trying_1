from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
   # path('join_hood/<str:id>/', views.join_hood, name='join_hood'),
    path('index_id/<int:id>/', views.detail_view, name='detail'),
]
