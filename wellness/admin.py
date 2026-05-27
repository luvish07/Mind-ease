from django.contrib import admin

from .models import GratitudeEntry


@admin.register(GratitudeEntry)
class GratitudeEntryAdmin(admin.ModelAdmin):
    list_display = ("text", "created_at")
    search_fields = ("text",)
    readonly_fields = ("created_at",)
