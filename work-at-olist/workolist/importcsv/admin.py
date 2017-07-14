from django.contrib import admin
from .models import Category, SubCategory, Channel

class ChannelAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Information:',{'fields': ['name', 'description']}),
        ('Category:',{'fields': ['category_channel'], 'classes': ['collapse']}),
    ]
    list_display = ('name', 'description')
    list_display_links = ('name', 'description')
    list_filter = ['name']
    search_fields = ['name']
    list_per_page = 20
    filter_horizontal = ['category_channel']


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Information:',{'fields': ['name', 'description']}),
        ('Sub Category:',{'fields': ['sub_category']}),
    ]
    list_display = ('name', 'description')
    list_filter = ['name']
    search_fields = ['name']
    list_per_page = 20
    filter_horizontal = ['sub_category']

class SubCategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Information:',{'fields': ['name', 'description']}),
    ]
    list_display = ('name', 'description')
    list_filter = ['name']
    search_fields = ['name']
    list_per_page = 20

admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Channel, ChannelAdmin)
