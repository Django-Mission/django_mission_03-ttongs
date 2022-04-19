from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic.list import ListView

from .models import Post #같은 패키지 안에 있기 때문에 . 사용

def index(request):
    return render(request, 'index.html')

def post_list_view(request):
    return render(request, 'posts/post_list.html') #settings의 TEMPLATES의 DIRS 경로 다음부터 써준다

def post_detail_view(request, id):
    return render(request, 'posts/post_detail.html')

def post_create_view(request):
    return render(request, 'posts/post_form.html')

def post_update_view(request, id):
    return render(request, 'posts/post_form.html')

def post_delete_view(request, id):
    return render(request, 'posts/post_confirm_delete.html')    

def url_view(request):
    print('url_view()')
    data = {'code':'001', 'msg': 'ok'}
    return HttpResponse('<h1>url_view</h1>')
    #return JsonResponse(data)

def url_parameter_view(request, username):
    print('url_parameter_view')
    print(f'username: {username}')
    print(f'request.GET: {request.GET}') #query string 내용 확인
    return HttpResponse(username)

def function_view(request):
    print(f'request.method: {request.method}')
    if request.method == 'GET':
        print(f'request.GET: {request.GET}') #data, resource를 받을 때 사용
    elif request.method == 'POST':
        print(f'request.POST: {request.POST}') #data를 추가, 수정, 삭제할 때 사용
    return render(request, 'view.html')


#class 기반 view
class class_view(ListView):
    model = Post
    template_name = 'cbv_view.html'