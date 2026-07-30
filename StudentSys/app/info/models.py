from django.db import models

from login.models import Student
# Create your models here.
# Create your models here.
class StudentInfo(models.Model):
    GENDER_CHOICES = (
        ('male', '男'),
        ('female', '女'),
    )

    student= models.OneToOneField(Student, on_delete=models.CASCADE, help_text="学生表一对一关系")
    gender = models.CharField(help_text='性别', max_length=6, choices=GENDER_CHOICES, null=True, blank=True)
    birthday = models.DateField(help_text='出生日期', null=True, blank=True)
    clazz = models.CharField(help_text='班级', max_length=50, null=True, blank=True)
    address = models.TextField(help_text='家庭住址', null=True, blank=True)
    avatar = models.CharField(help_text='学生照片', max_length=250)

    class Meta:
        db_table = 'tb_info'
        verbose_name = '学生详细信息'
        verbose_name_plural = '学生详细信息'

