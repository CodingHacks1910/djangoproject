from django.contrib import admin
from .models import Blog, Comment, UserProfileInfo
from django.db import models
from markdownx.admin import MarkdownxModelAdmin
from markdownx.widgets import AdminMarkdownxWidget
admin.site.site_header = 'Advice Lance'


admin.site.register(Blog, MarkdownxModelAdmin)
class Blog():
	list_filter = ['publish_date',]

class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
    
# class BlogAdmin(admin.ModelAdmin):
# 	list_filter = ['publish_date',]
# admin.site.register(Blog, BlogAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'email','active')
	list_filter = ('creadted',)

admin.site.register(UserProfileInfo)
