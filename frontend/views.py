from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from photos.models import Photo, Category

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
