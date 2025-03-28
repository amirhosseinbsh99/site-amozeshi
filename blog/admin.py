from django.contrib import admin

from .models import Course , Category, Comment, Article,Basket,BasketItem

# Register your models here.

admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Article)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'course', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
admin.site.register(Basket)
admin.site.register(BasketItem)

