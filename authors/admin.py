from django.contrib import admin

from authors.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'bio', 'author']
    list_display_links = ['bio', 'author']
    search_fields = 'author',
    list_filter = 'author',
