from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse


# Create your views here.
# 视图函数，和urls.py配合使用
def login(request):
    # return HttpResponse("登录页面")
    # return redirect("https://www.baidu.com")
    # return render(request, "login.html")
    # 判断是post请求还是get请求
    if request.method == "GET":
        return render(request, "login.html")
    else:
        # 去请求体中获取表单数据，再对表单数据进行校验
        username = request.POST.get("username")
        password = request.POST.get("pwd")

        # 去数据库中校验数据
        # 成功，跳转到首页，http://127.0.0.1:9000/user/list/
        # 不成功，返回登录页面，并提示用户
        if username == "root" and password == "123":
            # return redirect('/user/list/')
            return redirect('/index/')
        else:
            return render(request, "login.html", {"error": "用户名或密码错误！"})


def user_list(request):
    # 1、数据库获取的数据
    queryset = [
        {"id": "1", "phone": "13500000000", "city": "武汉"},
        {"id": "2", "phone": "13500000000", "city": "上海"},
        {"id": "3", "phone": "13500000000", "city": "北京"},
        {"id": "4", "phone": "13500000000", "city": "武汉"},
    ]
    return render(request, "user_list.html", {"queryset": queryset})


def index(request):
    # 数据库获取的数据
    data = [
        {"id": "1", "phone": "13500000000", "city": "武汉"},
        {"id": "2", "phone": "135002000000", "city": "上海"},
        {"id": "3", "phone": "13500030000", "city": "北京"},
        {"id": "4", "phone": "13500040000", "city": "武汉"},
    ]
    return render(request, "index.html", {"data": data})
