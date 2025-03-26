from rest_framework import serializers
from .models import Category, Photo

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'created_at']

class PhotoSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Photo
        fields = [
            'id', 'title', 'slug', 'description', 'image',
            'category', 'category_name', 'taken_date', 'location',
            'camera_model', 'lens_model', 'featured',
            'created_at', 'updated_at'
        ] 