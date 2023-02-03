from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('category/list/', views.CategoryListAPIView.as_view()),
    path('category/create/', views.CategoryCreateAPIView.as_view()),

    path('product/list/', views.ProductListAPIView.as_view()),
    path('product/list/<slug:category_slug>/', views.ProductListAPIView.as_view()),
    path('product/create/', views.ProductCreateAPIView.as_view()),

]