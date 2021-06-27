from django.contrib import admin
from .models import Category, News, Comments
# Register your models here.

admin.site.register(Category)

class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "add_time")

class CommentsAdmin(admin.ModelAdmin):
    list_display = ("news", "category", "comment")

admin.site.register(News)
admin.site.register(Comments)
