from django.contrib import admin

from blogs.models import Article, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    title = ['title', 'text', 'user']
    search_fields = ['title', 'user', 'text']
    list_filter = ['user']
    list_display = ['title', 'user']
    editable_list = ['title', 'text']
    inlines = [CommentInline,]

class CommentAdmin(admin.ModelAdmin):
    title = ['article', 'name', 'comment', 'created_on']
    search_fields = ['article', 'created_on']
    list_filter = ['article', 'created_on']
    list_display = ['name', 'article', 'created_on']
    editable_list = ['name', 'comment']

admin.site.register(Article, PostAdmin)
admin.site.register(Comment, CommentAdmin)
# Register your models here.
