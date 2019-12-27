from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from .models import MyUser
#from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from equipment.models import Equipment
from . import forms
from . import models
import random
from django.core.mail import EmailMultiAlternatives
# Create your views here.



#主页
def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'user/index.html')


#登陆页面
def login(request):
    if request.session.get('is_login', None):
        return redirect('/index/')
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
           username = login_form.cleaned_data.get('username')
           password = login_form.cleaned_data.get('password')
           if MyUser.objects.filter(username=username):
               user = authenticate(username=username, password=password)
               if user:
                    if user.is_active:
                        print(username, password)
                        request.session['is_login'] = True
                        request.session['user_id'] = user.id
                        request.session['user_name'] = username
                        return redirect('/index/')
               else:
                    message = '账号密码错误，请重新输入'
                    return render(request, 'user/login.html', locals())
           else:
               message = '用户不存在，请注册'
               return render(request, 'user/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'user/login.html', locals())


#注册页面
def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')

            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'user/register.html', locals())
            else:
                if MyUser.objects.filter(username=username):
                    message = '用户名已经存在'
                    return render(request, 'user/register.html', locals())

                if MyUser.objects.filter(email=email):
                    message = '该邮箱已经被注册了！'
                    return render(request, 'user/register.html', locals())
                user = MyUser.objects.create_user(username=username, password=password1, email=email)
                user.save()
                return redirect('/login/')
        else:
            return render(request, 'user/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'user/register.html', locals())


#退出
def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/login/")
    request.session.flush()
    return redirect("/login/")
#找回密码
def findpassword(request):
    button = '获取验证码'
    new_password = False
    if request.method == 'POST':
        username = request.POST.get('username', 'root')
        VerificationCode = request.POST.get('VerificationCode', '')
        password = request.POST.get('password', '')
        user = MyUser.objects.filter(username=username)
        # 用户不存在
        if not user:
            tips = '用户' + username + '不存在'
        else:
            # 判断验证码是否已发送
            if not request.session.get('VerificationCode', ''):
                # 发送验证码并将验证码写入session
                button = '重置密码'
                tips = '验证码已发送'
                new_password = True
                VerificationCode = str(random.randint(1000, 9999))
                request.session['VerificationCode'] = VerificationCode
                user[0].email_user('找回密码', VerificationCode)
            # 匹配输入的验证码是否正确
            elif VerificationCode == request.session.get('VerificationCode'):
                # 密码加密处理并保存到数据库
                dj_ps = make_password(password, None, 'pbkdf2_sha256')
                user[0].password = dj_ps
                user[0].save()
                del request.session['VerificationCode']
                tips = '密码已重置'
                return redirect('/login/')
            # 输入验证码错误
            else:
                tips = '验证码错误，请重新获取'
                new_password = False
                del request.session['VerificationCode']
    return render(request, 'user/findpassword.html', locals())
