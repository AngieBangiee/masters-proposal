from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'meta_title', 'meta_description', 'meta_title',)
    prepopulated_fields = {'slug': ('title',)}  # new
 
admin.site.register(Page, PageAdmin)