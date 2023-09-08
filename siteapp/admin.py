from django.contrib import admin
from .models import Countries


class CountriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    list_editable = ('is_published',)


admin.site.register(Countries, CountriesAdmin)
