# assignment/models.py

from django.db import models

class About(models.Model):
    about_heading = models.CharField(max_length=25)
    about_description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.about_heading

class SocialLink(models.Model):
    about = models.ForeignKey(About, related_name='social_links', on_delete=models.CASCADE)
    platform = models.CharField(max_length=20)  # Example: Facebook, Twitter, Instagram
    link = models.URLField()

    def __str__(self):
        return f"{self.platform} - {self.link}"
