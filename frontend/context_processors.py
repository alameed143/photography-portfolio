from .models import SiteSettings

def site_settings(request):
    """Add site settings to the template context."""
    try:
        settings = SiteSettings.objects.first()
    except:
        settings = None
    return {'site_settings': settings} 