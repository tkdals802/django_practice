from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question


@login_required(login_url='common:login')
def question_create(request):
    """
    pybo 질문 등록
    """
    print(request.method)
    if request.method == 'POST':#페이지를 POST방식으로 호출
        form = QuestionForm(request.POST) #전달받은 데이터로 폼의 값이 채워짐
        if form.is_valid():#폼의 데이터가 유효한지 검증
            question = form.save(commit=False) #commit=False는 임시저장을 의미
                                               # 이걸 하지 않으면 Question.create_date에 값이 저장되지 않음
                                               # 폼에는 현재 subject, content 필드만 있다.
            question.create_date = timezone.now()
            question.author = request.user
            question.save()
            return redirect('pybo:index')
    else:
        form=QuestionForm() #페이지를 GET방식으로 호출 -> 질문을 등록하는 화면 렌더링
    context = {'form':form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    """

    pybo 질문 수정
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다.')
        #messages모듈은 오류를 임의로 발생시키고 싶은 경우 사용
        return redirect('pybo:detail', question_id=question.id)

    if request.method=="POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form':form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    """

    pybo 질문 삭제
    """

    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')