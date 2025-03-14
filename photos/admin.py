from django.contrib import admin
from .models import Photo

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'upload_date', 'uploader')
    list_filter = ('upload_date', 'uploader')
    search_fields = ('name', 'uploader__username')
    date_hierarchy = 'upload_date'
