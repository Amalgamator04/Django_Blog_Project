from django.contrib import admin
from .models import Post

admin.site.site_header = 'Photo & Video Blog Administration'
admin.site.site_title = 'Photo & Video Blog Admin'
admin.site.index_title = 'Manage Blog Content'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'summary')
    list_filter = ('created_at', 'author')
    ordering = ('-created_at',)
