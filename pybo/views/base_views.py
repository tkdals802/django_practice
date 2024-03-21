from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question

def index(request):
    3/0
    """

    pybo 목록 출력
    """

    # 입력인자
    # localhost:8000/pybo/?page=1  에서 page값을 가져옴
    # page 파라미터가 없는 URL을 위해 기본값으로 1을 지정
    page = request.GET.get('page' ,'1')

    # 조회
    question_list = Question.objects.order_by('-create_date') # -는 역순을 의미

    # 페이징 처리
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    # p.133 파라미터 정리 or https://docs.djangoproject.com/en/5.0/ref/paginator/


    print(page_obj.number)
    context = {'question_list' :page_obj}
    # context에 question_list를 넣으면 전체 리스트를, page_obj를 넣으면 페이지를 보여줌

    # return HttpResponse("hello pybo")
    return render(request, 'pybo/question_list.html' ,context)


def detail(request, question_id):
    """

    pybo 내용 출력
    """

    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)