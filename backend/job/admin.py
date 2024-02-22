from django.contrib import admin

from .models import Job, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Job)
 