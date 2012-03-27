from django.contrib import admin
from cdealer.category.models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','remark')
    search_fields=('name',)

admin.site.register(Category,CategoryAdmin)
