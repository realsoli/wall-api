from django.urls import path
from . import views

urlpatterns = [
    path('list', views.AdListView.as_view()),
    path('create', views.AdCreateView.as_view()),
    path('detail/<int:pk>', views.AdDetailView.as_view()),
    path('search/', views.AdSearchView.as_view()),
]
