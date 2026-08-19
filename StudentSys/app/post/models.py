from django.db import models
from login.models import Student


class Post(models.Model):
    author = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField('标题', max_length=100)
    content = models.TextField('内容')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '帖子'
        verbose_name_plural = '帖子'


class PostMedia(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('image', '图片'),
        ('video', '视频'),
        ('file', '文件'),
    ]

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='media')
    media_type = models.CharField('媒体类型', max_length=20, choices=MEDIA_TYPE_CHOICES, default='file')
    file = models.FileField('文件', max_length=250, null=True, blank=True, upload_to='post/')

    class Meta:
        verbose_name = '帖子媒体'
        verbose_name_plural = '帖子媒体'