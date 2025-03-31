from django.contrib import admin
from .models import Category, Type, Article

admin.site.register(Category)
admin.site.register(Type)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'type', 'born', 'died', 'nationality', 
                    'known_for', 'notable_work', 'about', 'year', 'medium', 
                    'dimensions', 'location', 'designed_by', 'developer')

    readonly_fields = ('category', 'type', 'name', 'born', 'died', 'nationality', 
                       'known_for', 'notable_work', 'about', 'year', 'medium', 
                       'dimensions', 'location', 'designed_by', 'developer')

    def has_delete_permission(self, request, obj=None):
        # Only allow delete for staff users
        return request.user.is_staff
