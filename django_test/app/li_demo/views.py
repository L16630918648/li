from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("<h1>你好 Django</h1>")

def inf_out(request, name, age):
    return HttpResponse(f"<p>姓名:{name}<br>年龄:{age}</p>")

def postion(request, x, y):
    return HttpResponse(f"<p align='center'>坐标：{x},{y}</p>")
