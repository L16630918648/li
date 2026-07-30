from django.db import models

# Create your models here.
# login app应用>/models.py

class Student(models.Model):
    student_id = models.CharField(
        verbose_name='学号',
        max_length=20,
        unique=True,
        help_text='学生唯一学号'
    )

    name = models.CharField(
        verbose_name='姓名',
        max_length=50
    )

    phone = models.CharField(
        verbose_name='手机号码',
        max_length=11,
        unique=True,
    )

    email = models.EmailField(
        verbose_name='邮箱',
        unique=True,
    )

    password = models.CharField(
        verbose_name='密码',
        max_length=16
    )

    created_at = models.DateTimeField(
        verbose_name='创建时间',
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name='更新时间',
        auto_now=True
    )

    class Meta:
        db_table = 'tb_student'
        verbose_name = '学生信息'
        verbose_name_plural = '学生信息'

