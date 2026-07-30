import os

from django.conf import settings
from django.db import transaction
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse

from info.models import StudentInfo
from login.models import Student


# Create your views here.
def index(request):
    student_id = request.session.get("student_id", None)
    student_data = Student.objects.filter(student_id=student_id)
    if not student_data.exists():
        return render(request, "login.html")
    student_data[0].password = "null"

    # 查询一下学生信息表
    student_info = StudentInfo.objects.filter(student=student_data[0])
    if student_info.exists():
        student_info = student_info[0]
    return render(
        request,
        "index.html",
        {
            "student_data": student_data[0],
            "student_info": student_info,
        }
    )

def info_api(request):
    if request.method == "POST":
        # 数据重新写入
        file = request.FILES.get("avatar", None)
        gender = request.POST.get("gender", None)
        birthday = request.POST.get("birthday", None)
        clas = request.POST.get("class", None)
        email = request.POST.get("email", None)
        phone = request.POST.get("phone", None)
        address = request.POST.get("address", None)

        # 下载文件
        if file:
            file_path = os.path.join(settings.MEDIA_ROOT, "avatars", file.name)
            with open(file_path, "wb") as f:
                # 安全分块读取
                for chunk in file.chunks():
                    # 将数据写入到内存中
                    f.write(chunk)
            save_path = os.path.join(settings.MEDIA_URL, "avatars", file.name)
        student_id = request.session.get("student_id", None)
        # 使用事务
        with transaction.atomic():
            # 先更新学生数据
            student_data = Student.objects.filter(student_id=student_id)
            student_data.update(
                phone=phone,
                email=email,
            )
            # 在更新信息数据
            student_info = StudentInfo.objects.filter(student=student_data[0])
            if not file:
                save_path = student_info[0].avatar

            if student_info.exists():
                # 更新数据
                student_info.update(avatar=save_path, gender=gender, birthday=birthday, clazz=clas, address=address)
            else:
                # 插入数据
                StudentInfo.objects.create(student=student_data[0], avatar=save_path, gender=gender, birthday=birthday, clazz=clas, address=address)

        return redirect(reverse('index'))

    return HttpResponseForbidden()
