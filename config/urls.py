from django.contrib import admin
from django.urls import path, include

from posts.views import index, url_parameter_view, url_view, function_view, class_view #다른 곳에 있는 함수, 클래스이므로 import 해주어야 함.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('url/', url_view), #list는 맨 뒤에 ,(콤마) 찍어주기
    path('url/<int:username>/', url_parameter_view),
    path('fbv/', function_view),
    path('cbv/', class_view.as_view()), #클래스는 .as_view() 해줘야 함
    path('', index, name='index'),
    path('posts/', include('posts.urls', namespace='posts')),

]
