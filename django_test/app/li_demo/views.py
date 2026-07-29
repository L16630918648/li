from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.urls import reverse
import datetime
import json
import os


# Create your views here.
def if_for(request):
    dict = {
        "list" : ["Bob","John","Alice"],
        "score" :45,
    }
    return render(request,"if_for.html",dict)

def room(request, name):
    return HttpResponse(f"<h1>这里是{name}的个人空间</h1>")

def page_GET(request):
    name = request.GET.getlist("name","None")
    age = request.GET.get("age","None")
    sex = request.GET.get("sex","None")
    txt = f"<div>姓名:{name}<br>年龄:{age}<br>性别:{sex}<div>"
    return HttpResponse(txt)

def index_redirect(request):
    print("正在跳转")
    return redirect(reverse("room", args=["Li"]))

def page_2006(request):
    url = reverse('first')
    return HttpResponseRedirect(url)

def back_first(request):
    return render(request,"hello.html")

def hello(request):
    html = "<h1>你好 Django</h1>"
    return HttpResponse(html,content_type="text/html;charset=utf-8",status=200)

def inf_out(request, name, age):
    return HttpResponse(f"<p>姓名:{name}<br>年龄:{age}</p>")

def postion(request, x, y):
    return HttpResponse(f"<p align='center'>坐标：{x},{y}</p>")

def time(request): 
    new = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    txt = f"服务器当前时间：{new}"
    return HttpResponse(txt,content_type="text/plain;charset=utf-8",status=200)

def api_info(request):
    data = {
        "name":"dolphin",
        "age":"21",
        "path":request.path,
    }
    json_info = json.dumps(data, ensure_ascii=False)
    return HttpResponse(json_info,content_type="application/json;charset=utf-8",status=200)

@csrf_exempt
def file_page(request):
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == 'POST':
        file = request.FILES["myfile"]
        print(F"上传文件名是：{file.name}")
        print(f"文件的字节大小：{file.size}")
        filename = os.path.join(settings.MEDIA_ROOT, file.name)
        with open(filename, "wb") as f:
            for chunk in file.chunks():
            # 将数据写入到内存中
                f.write(chunk)
        return HttpResponse('接受文件：' + file.name + "成功")


def file_download(request, file_name):
    file_path = os.path.join(settings.BASE_DIR, 'media', file_name)

    if not os.path.exists(file_path):
        return HttpResponse('文件不存在', status=404)

    def file_iterator(path, chunk_size=8192):
        # 以二进制只读模式打开文件
        with open(path, 'rb') as f:
            # 无限循环，直到文件读完
            while True:
                # 每次读取 8 KB
                chunk = f.read(chunk_size)
                # 没有数据表示读到 EOF
                if not chunk:
                    break
                # 生成器逐块产出数据
                yield chunk

    # 构造流式下载响应
    response = HttpResponse(
        file_iterator(file_path),  # 给 HttpResponse 一个可迭代对象即可流式输出
        content_type='application/octet-stream'  # 通用二进制流
    )
    # 设置 Content-Disposition 让浏览器弹出“另存为”对话框
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response
