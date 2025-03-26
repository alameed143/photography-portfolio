from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from rest_framework import generics
from photos.models import Photo, Category
from .serializers import PhotoSerializer, CategorySerializer, ContactSerializer

# Create your views here.

class HomeView(TemplateView):
    template_name = 'frontend/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_photos'] = Photo.objects.filter(featured=True)[:6]
        context['categories'] = Category.objects.all()[:4]
        return context

class GalleryView(ListView):
    template_name = 'frontend/gallery.html'
    model = Photo
    context_object_name = 'photos'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category__slug=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class AboutView(TemplateView):
    template_name = 'frontend/about.html'

class ContactView(TemplateView):
    template_name = 'frontend/contact.html'

# API views
class PhotoListCreateView(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class PhotoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ContactCreateView(generics.CreateAPIView):
    serializer_class = ContactSerializer
