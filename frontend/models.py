from django.db import models

class SiteSettings(models.Model):
    site_logo = models.ImageField(upload_to='site/', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Site Settings"

    def save(self, *args, **kwargs):
        if SiteSettings.objects.exists() and not self.pk:
            # If a SiteSettings instance exists and we're trying to create a new one
            return
        return super(SiteSettings, self).save(*args, **kwargs)
