from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm

# Create your views here.

''' 
def signup(request):
    """

    회원가입
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_date.get('password1')
            user = authenticate(username=username, password=raw_password) #회원가입 후 자동 로그인
            login(request, user)
            return redirect('index')
        else:#GET 요청일 경우 common/signup.html 반환
            form = UserForm()
        return render(request, 'common/signup.html', {'form':form})
'''
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

def page_not_found(request, exception):
    """

    404 Page not found
    """

    return render(request, 'common/404.html',{})