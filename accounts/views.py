from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_GET
# AuthenticationForm 로그인할때 필요 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# login logout 필요
from django.contrib.auth import login as auth_login, logout as auth_logout 
from django.contrib.auth.decorators import login_required 
# 회원정보 수정 없어서 필요없음 
from .forms import CustomUserChangeForm


# create 복사하고할것 
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        # request 
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            #
            auth_login(request, form.get_user())
            # 장고 DB 의 세션과 웹 쿠키가 남아있으면 로그인된 상태로 서버가 켜짐 / 세션을 DB 가 아닌 메모리에 저장한다면 자동 로그아웃 
            # GET 은 query 를 받아오기 위한 함수 / 일반적으로 GET 요청으로 오기 때문에 명시적으로 표시됨 
            # next_page = request.GET.get('next')
            # return redirect(next_page or 'articles:index')
            return redirect('articles:index')
    else:
        #
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def logout(request):
    #
    auth_logout(request)
    return redirect('articles:index')


# require_POST
@require_POST
def delete(request):
    if request.user.is_authenticated:
    # 
        request.user.delete()
    #
    return redirect('articles:index')
