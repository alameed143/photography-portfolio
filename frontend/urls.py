from django.urls import path
from . import views

urlpatterns = [
    # Frontend routes
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
    # API routes
    path('api/photos/', views.PhotoListCreateView.as_view(), name='photo-list-create'),
    path('api/photos/<int:pk>/', views.PhotoDetailView.as_view(), name='photo-detail'),
    path('api/categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('api/categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('api/contact/', views.ContactCreateView.as_view(), name='contact-create'),
] 