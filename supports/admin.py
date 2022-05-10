from django.contrib import admin

# Register your models here.
from .models import Answer, Faq, Inquiry #같은 경로 선상에 있기 때문에 .(현재위치)


class AnswerInline(admin.TabularInline):
    model = Answer
    verbose_name = '답변'
    verbose_name_plural = '답변'

@admin.register(Faq)
class InquiryModelAdmin(admin.ModelAdmin):
    list_display = ('id','question','category','final_created_at')
    list_filter = ('category',) # ,(콤마) 붙이기
    search_fields = ('id', 'question')
    readonly_fields = ('created_at', )

@admin.register(Inquiry)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','created_at','writer')
    list_filter = ('category',) # ,(콤마) 붙이기
    search_fields = ('id', 'title', 'email', 'phone',)
    readonly_fields = ('created_at', )
    inlines = [AnswerInline]