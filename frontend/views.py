from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from rest_framework import generics
from photos.models import Photo, Category, Contact
from .serializers import PhotoSerializer, CategorySerializer, ContactSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
import json
import os

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

def home(request):
    """Home page view"""
    return render(request, 'frontend/home.html')

def gallery(request):
    """Gallery page view"""
    return render(request, 'frontend/gallery.html')

def about(request):
    """About page view"""
    return render(request, 'frontend/about.html')

def contact(request):
    """Contact page view"""
    return render(request, 'frontend/contact.html')

def frontend_login(request):
    """Frontend login view"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'message': 'Invalid credentials'})
    return render(request, 'frontend/login.html')

def frontend_logout(request):
    """Frontend logout view"""
    logout(request)
    return redirect('home')

@csrf_exempt
@login_required
def update_content(request):
    if request.method == 'POST' and request.user.is_superuser:
        data = json.loads(request.body)
        element_id = data.get('element_id')
        content = data.get('content')
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Unauthorized'})

@csrf_exempt
@login_required
def upload_image(request):
    if request.method == 'POST' and request.user.is_superuser:
        image = request.FILES.get('image')
        image_type = request.POST.get('type')
        
        if not image:
            return JsonResponse({'success': False, 'error': 'No image provided'})
            
        # Define the path based on image type
        if image_type == 'hero':
            path = 'frontend/static/images/hero.jpg'
        elif image_type == 'about':
            path = 'frontend/static/images/about.jpg'
        else:
            path = f'frontend/static/images/{image.name}'
            
        # Save the file
        try:
            if default_storage.exists(path):
                default_storage.delete(path)
            default_storage.save(path, image)
            return JsonResponse({'success': True, 'path': path})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
            
    return JsonResponse({'success': False, 'error': 'Invalid request'})
