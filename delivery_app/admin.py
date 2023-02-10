from django.contrib import admin

from delivery_app.models import Category, Dish, Cart, Order, Logo


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url_category': ('title',)}
    list_display = ('title', 'url_category', 'description_category', 'image_category',)
    list_display_links = ('title', 'description_category')
    search_fields = ('title', 'description_category',)


class DishAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url_dish': ('title',)}
    list_display = ('title', 'url_dish', 'description_dish', 'image_dish', 'category', 'price',)
    list_display_links = ('title', 'description_dish')
    search_fields = ('title', 'description_dish',)


class CartAdmin(admin.ModelAdmin):
    list_display = ('published_at', 'active_status', 'count_of_dishes', 'dish', 'user',)
    list_display_links = ('active_status', 'count_of_dishes')
    search_fields = ('active_status', 'count_of_dishes',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('owner', 'order_creation_time', 'list_of_dishes', 'order_status', 'payment_method', 'user_phone', 'address', 'user_comment',)
    list_display_links = ('list_of_dishes', 'order_status', 'payment_method',)
    search_fields = ('list_of_dishes', 'order_status', 'payment_method',)


class LogoAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Logo, LogoAdmin)
