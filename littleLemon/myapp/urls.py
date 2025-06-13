from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('menu/<int:pk>/', views.SingleMenuView.as_view(), name='single_menu'),
    path('secured-view/',views.secured_view,name='secured-view')
    # Add more URL patterns as needed
]