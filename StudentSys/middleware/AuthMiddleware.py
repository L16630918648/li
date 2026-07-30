# 导入模块
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


# 创建一个类继承MiddlewareMixin方法
class AuthMiddleware(MiddlewareMixin):
    # 注：中间件中的大多数方法在返回None时表示忽略当前操作进入下一项事件，
    # 当返回 HttpResponse 对象时表示此请求结束，直接返回给客户端
    # 不是所有方法都需要编写，选择自己适合可以实现业务的方法重写

    # 重写方法
    # 执行路由之前被调用，在每个请求上调用，返回 None 或 HttpResponse 对象
    # 在视图之前执行
    def process_request(self, request):
        # 获取 session
        student_id = request.session.get("student_id", None)
        # 判断是否访问列表里边的连接，如果是则允许访问
        path = request.path_info.split("/")[1]
        if path in "".join([
            "login/", "registered/",
            "api/", "admin/"
        ]):
            # 如果不为空则允许访问
            if student_id:
                if request.path_info in [
                    "/login/", "/registered/"
                ]:
                    return redirect(reverse('index'))
            return
        # 如果不为空则允许访问
        if student_id:
            return
        # 如果为空则要求对方登录
        return redirect(reverse('login'))

