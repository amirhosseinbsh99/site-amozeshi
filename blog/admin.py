from django.contrib import admin

from .models import Post , Category, Comment, Addarticle

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Addarticle)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
