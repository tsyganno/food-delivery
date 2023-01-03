from django.contrib import admin

from delivery_app.models import Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url_category': ('name',)}
    list_display = ('name', 'url_category', 'description_category', 'image_category',)
    list_display_links = ('name', 'description_category')
    search_fields = ('name', 'description_category',)


admin.site.register(Category, CategoryAdmin)
