from django.db import models
from login.models import Student
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(Student, on_delete = models.CASCADE, related_name = 'posts')
    title = models.CharField('标题', max_length=100)
    content = models.TextField('内容')
    create_at = models.DateTimeField('创建时间',auto_now = True)
    updata_at = models.DateTimeField('创建时间',auto_now_add=True)
