from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title', 'time_create')
    prepopulated_fields = {'slug': ('title', )}
    fields = ('title', 'slug', 'cat', 'content', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)