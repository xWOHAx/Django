from django.contrib import admin
from main.models import Main, Banner

@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)