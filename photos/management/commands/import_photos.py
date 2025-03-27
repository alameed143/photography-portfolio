import os
from django.core.management.base import BaseCommand
from django.core.files import File
from photos.models import Photo, Category
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Import photos from a directory into the gallery'

    def add_arguments(self, parser):
        parser.add_argument('directory', type=str, help='Directory containing photos')
        parser.add_argument('--category', type=str, help='Category name for the photos', default='Uncategorized')

    def handle(self, *args, **options):
        directory = options['directory']
        category_name = options['category']

        # Create or get the category
        category, created = Category.objects.get_or_create(
            name=category_name,
            defaults={'slug': slugify(category_name)}
        )

        # List all image files in the directory
        valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
        for filename in os.listdir(directory):
            ext = os.path.splitext(filename)[1].lower()
            if ext in valid_extensions:
                filepath = os.path.join(directory, filename)
                
                # Create title from filename
                title = os.path.splitext(filename)[0].replace('_', ' ').title()
                
                # Check if photo already exists
                if not Photo.objects.filter(title=title).exists():
                    with open(filepath, 'rb') as f:
                        photo = Photo(
                            title=title,
                            slug=slugify(title),
                            category=category,
                            description=f'Photo of {title}'
                        )
                        photo.image.save(filename, File(f), save=True)
                        self.stdout.write(self.style.SUCCESS(f'Successfully imported {filename}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Skipped {filename} - already exists')) 