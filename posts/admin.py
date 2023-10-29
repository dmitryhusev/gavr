from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Post


class PostAdmin(ModelAdmin):
    model = Post
    list_display = ('title', 'author', 'date_added')
    ordering = ("title",)
    search_fields = ('title',)


admin.site.register(Post, PostAdmin)
