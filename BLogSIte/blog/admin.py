from django.contrib import admin
from .models import Post, normUser, Comment, feedbacks


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    
class NormUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'fullname')
    search_fields = ['username', 'email', 'phone']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_on')
    search_fields = ['user__username', 'post__title']

class FeedbacksAdmin(admin.ModelAdmin):
    list_display = ('content', 'annonuser', 'created_at')


admin.site.register(Post, PostAdmin)
admin.site.register(normUser, NormUserAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(feedbacks, FeedbacksAdmin)