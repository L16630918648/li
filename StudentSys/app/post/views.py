from django.shortcuts import render, redirect
from django.urls import reverse
from login.models import Student
from .models import Post

# Create your views here.
def get_login_student(request):
    student_id = request.session.get("student_id")
    if not student_id:
        return None
    return Student.objects.filter(student_id = student_id).first()

def post(request):
    posts = Post.objects.select_related("author").all().order_by('-id')
    student = get_login_student(request)
    return render(request, 'post.html', {'posts': posts, 'student': student})

def post_create_page(request):
    student = get_login_student(request)
    if not student:
        return redirect(reverse("login"))
    return render(request, 'post_create.html', {'student': student})

def post_create_api(request):
    student = get_login_student(request)
    if not student:
        return redirect(reverse('login'))
    if request.method != "POST":
        return redirect(reverse("create"))

    title = request.POST.get("title", "").strip()
    content = request.POST.get("content", "").strip()
    if not title or not content:
        return render(request, "post_create.html", {"err": "标题和内容不能为空"})

    Post.objects.create(
        author=student,
        title=title,
        content=content
    )
    return redirect(reverse("mine"))

def post_mine(request):
    student = get_login_student(request)
    if not student:
        return redirect(reverse('login'))
    posts = Post.objects.filter(author=student).order_by('-id')
    return render(request, 'post_mine.html', {'posts': posts, 'student': student})
