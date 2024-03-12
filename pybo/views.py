from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm #forms.py에서 QuestionForm import
from django.core.paginator import Paginator #페이징을 위한 함수


# Create your views here.
from django.http import HttpResponse

def index(request):
    """ 
    
    pybo 목록 출력
    """

    #입력인자
    #localhost:8000/pybo/?page=1  에서 page값을 가져옴
    #page 파라미터가 없는 URL을 위해 기본값으로 1을 지정
    page = request.GET.get('page','1')

    #조회
    question_list = Question.objects.order_by('-create_date') #-는 역순을 의미

    #페이징 처리
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    #p.133 파라미터 정리 or https://docs.djangoproject.com/en/5.0/ref/paginator/


    print(page_obj.number)
    context = {'question_list':page_obj}
    #context에 question_list를 넣으면 전체 리스트를, page_obj를 넣으면 페이지를 보여줌

    #return HttpResponse("hello pybo")
    return render(request, 'pybo/question_list.html',context)

def detail(request, question_id):
    """
    
    pybo 내용 출력
    """

    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)

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
            question.save()
            return redirect('pybo:index')
    else:
        form=QuestionForm() #페이지를 GET방식으로 호출 -> 질문을 등록하는 화면 렌더링
    context = {'form':form}
    return render(request, 'pybo/question_form.html', context)

def answer_create(request,question_id):
    """

    pybo 답변 등록
    """

    question = get_object_or_404(Question, pk=question_id)
    print(question)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form=AnswerForm()
    context = {'question':question, 'form':form}
    return render(request, 'pybo/question_detail.html', context)
