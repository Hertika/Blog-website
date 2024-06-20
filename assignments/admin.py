# assignment/admin.py

from django.contrib import admin
from .models import About, SocialLink

class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('about_heading', 'created_at', 'updated_at')
    search_fields = ('about_heading',)
    readonly_fields = ('created_at', 'updated_at')
    inlines = [SocialLinkInline]

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('about', 'platform', 'link')
    list_filter = ('platform',)
