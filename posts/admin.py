from csv import list_dialects
from django.contrib import admin

from .models import Post, Comment #같은 경로 선상에 있기 때문에 .(현재위치)


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 5
    min_num = 3
    max_num = 5
    verbose_name = '댓글'
    verbose_name_plural = '댓글'

# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id','content','image','content','created_at','view_count','writer')
    #list_editable = ('content',)
    list_filter = ('created_at',) # ,(콤마) 붙이기
    search_fields = ('id', 'writer__username')
    readonly_fields = ('created_at', )
    inlines = [CommentInline]

#admin.site.register(Comment)