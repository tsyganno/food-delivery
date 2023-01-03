from django.contrib import admin

from delivery_app.models import Category, Dish


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url_category': ('name',)}
    list_display = ('name', 'url_category', 'description_category', 'image_category',)
    list_display_links = ('name', 'description_category')
    search_fields = ('name', 'description_category',)


class DishAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url_dish': ('title',)}
    list_display = ('title', 'url_dish', 'description_dish', 'image_dish', 'category', 'price',)
    list_display_links = ('title', 'description_dish')
    search_fields = ('title', 'description_dish',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Dish, DishAdmin)
