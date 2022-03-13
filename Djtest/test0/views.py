from django.shortcuts import render, HttpResponse,redirect
import json
from django.http import JsonResponse
from django.views.generic import View
from django.forms.models import model_to_dict
from .models import User,Healthdata
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return HttpResponse("欢迎使用")

def user_list(request):
    return HttpResponse("用户列表")

def sth(request):
    print(request.method)
    return redirect("https://www.baidu.com")

def login(request):
    if request.method=="GET":
        return render(request,"login.html")
    else:
        username=request.POST.get("user")
        password=request.POST.get("pwd")

        if  username=="kexin" and password=="0807":
            return HttpResponse("  *★,°*:.☆(￣▽￣)/$:*.°★* 。")
        elif username=="weichen" and password=="0807":
            return HttpResponse("登陆成功")
        else:
            return HttpResponse("请重试")
class UsersView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(UsersView, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, pk=0):
        if pk:
            try:
                user = User.objects.get(pk=pk)
                user = model_to_dict(user)
                return JsonResponse({'code': 200, 'message': 'success', 'data': user}, status=200)
            except User.DoesNotExist:
                return JsonResponse({'code': 404, 'message': '用户不存在'}, status=200)
        data = json.loads(request.body) if request.body else {}
        users = list(User.objects.filter(**data).all().values())
        return JsonResponse({'code': 200, 'message': 'success', 'data': users}, status=200)
    def post(self, request):
        data = json.loads(request.body)
        user = User.objects.create(**data)
        user = model_to_dict(user)
        return JsonResponse({'code': 201, 'message': 'created', 'data': user}, status=201)
       
    def put(self, request, pk=0):
        data = json.loads(request.body)
        user = User.objects.get(pk=pk)
        for key, value in data.items():
            setattr(user, key, value)
        user.save()
        user = model_to_dict(user)
        return JsonResponse({'code': 200, 'message': 'updated', 'data': user}, status=200)
    def delete(self, request, pk=0):
        user = User.objects.get(pk=pk)
        user.delete()
        return JsonResponse({'code': 204, 'message': 'deleted'}, status=204)



class HealthdataView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(HealthdataView, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, pk=0):
        if pk:
            try:
                user = Healthdata.objects.get(pk=pk)
                user = model_to_dict(user)
                return JsonResponse({'code': 200, 'message': 'success', 'data': user}, status=200)
            except Healthdata.DoesNotExist:
                return JsonResponse({'code': 404, 'message': '用户不存在'}, status=200)
        data = json.loads(request.body) if request.body else {}
        users = list(Healthdata.objects.filter(**data).all().values())
        return JsonResponse({'code': 200, 'message': 'success', 'data': users}, status=200)
    def post(self, request):
        data = json.loads(request.body)
        user = Healthdata.objects.create(**data)
        user = model_to_dict(user)
        return JsonResponse({'code': 201, 'message': 'created', 'data': user}, status=201)
       
    def put(self, request, pk=0):
        data = json.loads(request.body)
        user = Healthdata.objects.get(pk=pk)
        for key, value in data.items():
            setattr(user, key, value)
        user.save()
        user = model_to_dict(user)
        return JsonResponse({'code': 200, 'message': 'updated', 'data': user}, status=200)
    def delete(self, request, pk=0):
        user = Healthdata.objects.get(pk=pk)
        user.delete()
        return JsonResponse({'code': 204, 'message': 'deleted'}, status=204)