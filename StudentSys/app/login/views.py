# <login app应用>/views.py

import os
from django.urls import reverse
from django.utils import timezone
from utils.utils import generate_time_student_id
from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponseForbidden, HttpResponseServerError, JsonResponse
from django.core.mail import send_mail
from .models import Student, Verifition
import random, string
from datetime import timedelta
# 注册主页
def registered_index(request):
    return render(request, "registered.html")

# 插入表单接口
def registered_add(request):
    if request.method == "POST":
        name=request.POST["name"]
        phone=request.POST["phone"]
        email=request.POST["email"]
        password=request.POST["password"]
        input_verification=request.POST["verification"]
        v_obj = Verifition.objects.filter(email=email).first()
        if not v_obj:
            return JsonResponse({"code": 400,"message": "请先获取验证码"})        
        verification = v_obj.verifition
        #判断验证码有效性：
        now = timezone.now()
        creat_time = v_obj.creat_time
        valid_time = timedelta(minutes=5)
        if now - creat_time > valid_time:
            return JsonResponse({"code": 400, "message": "完整码过期"})
        #验证码正确：
        if input_verification.strip().lower() != verification.lower():
            return JsonResponse({"code": 400, "message": "验证码错误"})

        if Student.objects.filter(phone=phone).exists():
            return JsonResponse({"code": 400, "field": "phoneErr", "message": "手机号已被注册"})
        # 随机生成一个学号
        student_id = generate_time_student_id()
        # 插入数据
        Student.objects.create(
            student_id=student_id,
            name=name,
            phone=phone,
            email=email,
            password=password,
        )
        # 插入成功 就直接跳到首页页了
        request.session["student_id"] = student_id
        return JsonResponse({"code": 200, "message": "注册成功", "redirect": reverse("index")})
    return HttpResponseForbidden()


def login(request):
    return render(request, "login.html")

def login_out(request):
    request.session.flush()
    return redirect('login')

def login_api(request):
    name = request.GET["name"]
    password = request.GET["password"]

    # 先判断账号是否存在
    user = Student.objects.filter(
        Q(student_id__exact=name) |
        Q(phone__exact=name) |
        Q(email__exact=name)
    )
    if not user.exists():
        return render(request, "login.html", {
            "nameErr": "账号不存在",
            "userName": name,
            "pwd": password,
        })

    queryset = Student.objects.filter(
        Q(password__exact=password),
        Q(student_id__exact=name) |
        Q(phone__exact=name)  |
        Q(email__exact=name)
    )
    print(queryset)
    if queryset.exists():
        request.session["student_id"] = queryset[0].student_id
        return redirect(reverse('index'))


    return render(request, "login.html", {
        "nameErr": "请输入正确的账号密码",
        "userName": name,
        "pwd": password,
    })


def email_send_code(request):
    email = request.GET.get("email")
    if not email:
        return JsonResponse({"code": 400, "message": "邮箱为空"})
    verifition = ''.join(random.sample(string.hexdigits, 4))
    Verifition.objects.update_or_create(email=email, defaults={'verifition':verifition, 'creat_time': timezone.now()})
    send_mail(subject="来自大学广场的验证码：",message=f"验证码:{verifition}", from_email=None, recipient_list=[email])
    return JsonResponse({"code": 200,"message": "验证码已发送"})