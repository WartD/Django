from django.contrib import admin

from videos.models import Movie, Customer


class MovieAdmin(admin.ModelAdmin):
    title = ['release_year', 'title', 'length', 'tags']
    search_fields = ['title', 'length', 'tags', 'release_year']
    list_filter = ['tags', 'release_year']
    list_display = ['title', 'tags', 'release_year']
    list_editable = ['tags', 'release_year']

class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'phone']
    list_filter = ['first_name']
    list_display = ['first_name', 'last_name', 'phone']
    list_editable = ['phone']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Customer, CustomerAdmin)
# Register your models here.

