from django.contrib import admin

# Register your models here.
from .models import Answer, Faq, Inquiry #같은 경로 선상에 있기 때문에 .(현재위치)

admin.site.register(Faq)
admin.site.register(Inquiry)
admin.site.register(Answer)